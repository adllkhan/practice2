def chessComparisons():
    coordinates = input()  # For example a 1 c 2
    if(isinstance(coordinates.split()[0], str) == True and isinstance(coordinates.split()[1], int) == True and isinstance(coordinates.split()[2], str) == True and isinstance(coordinates.split()[3], int) == True):
        if(ord(coordinates.split()[0])-96 <= 8 and int(coordinates.split()[1]) <= 8 and ord(coordinates.split()[2])-96 <= 8 and int(coordinates.split()[3]) <= 8):
            square1 = int(ord(coordinates.split()[0])-96) + int(coordinates.split()[1])
            square2 = int(ord(coordinates.split()[2])-96) + int(coordinates.split()[3])
            if(square1 % 2 == 0):
                if(square2 % 2 == 0):
                    print("both on black square")
                else:
                    print(coordinates.split()[0], coordinates.split()[1] ,"on black square and", coordinates.split()[2], coordinates.split()[3], "on white square")
            else:
                if(square2 % 2 == 0):
                    print(coordinates.split()[0], coordinates.split()[1] ,"on white square and", coordinates.split()[2], coordinates.split()[3], "on black square")
                else:
                    print("both on white square")
        else:
            print("input values <= 8 and <= h, try again.")
            return chessComparisons()
    else:
        print("first must be a character, then number, try again.")
        return chessComparisons()


chessComparisons()