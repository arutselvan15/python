
street = [i for i in range(-20,20)]
print (street)

testCase = int(input(''))

while testCase:
    home = int(input(''))

    position = 0
    moveStep = 1

    print ("Home : {}".format(home))
    stops = 0
    tracker = []
    setFlag = False
    while position != home:
        stops += 1
        if setFlag:
            pass
        if (position + moveStep) <= home :
            position += moveStep
        else:
            position -= moveStep
        moveStep += 1
        tracker.append(position)
    print ("Route : {}".format(tracker))
    print ("No. of stops : {}".format(stops))
    testCase -= 1 
