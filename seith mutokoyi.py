def join_compute():
    import math
    cx1 = float(input("enter cx1 coordinate"))
    cx2 = float(input("enter cx2 coordinate"))
    cy1 = float(input("enter cy1 coordinate"))
    cy2 = float(input("enter cy2 coordinate"))
    differenceX = cx2-cx1
    differenceY = cy2-cy1
    distance = math.sqrt((differenceY**2)+(differenceX**2))#distance in meters
    print(distance)
    direction = math.degrees(math.tanh(differenceY/differenceX))#direction in degrees
    if differenceX < 0 and differenceY < 0:
       print(direction-180)
    elif differenceX > 0 and differenceY < 0:
        print(direction+360)
    elif differenceX < 0 and differenceY > 0:
        print(direction+180)
    else:
        print(direction)
join_compute()

