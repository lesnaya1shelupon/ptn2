m = int(input("Write month number: "))

    if  0 < m <= 12:
        if m == 1:
            print("January")
        elif m == 2:
            print("February")
        elif m == 3:
            print("March")
        elif m == 4:
            print("April")
        elif m == 5:
            print("May")
        elif m == 6:
            print("June")
        elif m == 7:
            print("July")
        elif m == 8:
            print("August")
        elif m == 9:
            print("September")
        elif m == 10:
            print("October")
        elif m == 11:
            print("November")
        elif m == 12:
            print("December")

    else:
        print("Write number from 1 to 12")
