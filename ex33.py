
def doTimes(times, incr=1):
    numbers = [ ]
    for i in range(0, times, incr):
        print "at the top i is %d" % i 
        numbers.append(i)

        i = i + incr
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num


doTimes(6)


