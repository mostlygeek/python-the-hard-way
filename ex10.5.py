# Let's make a spinning thing that takes up 100% cpu
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
