from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# This isn't necesary... `w` mode, will truncate automatically if 
# the file exists ..
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# write it out as a single line...
target.write( "%s\n%s\n%s\n" % ( line1, line2, line3) )

print "And finally, we close it."
target.close()

print "Let's read it back out again to make sure it is ok"

reopened = open(filename, 'r')
print reopened.read()

