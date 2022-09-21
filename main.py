def chessComparisons():
    coordinates = input()  # For example a 1 c 2
    if(0 < ord(coordinates.split()[0])-96 <= 8 and 0 < int(coordinates.split()[1]) <= 8 and 0 < ord(coordinates.split()[2])-96 <= 8 and 0 < int(coordinates.split()[3]) <= 8):
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
        print("input values from 1 to 8 and from a to h, \ntry again.")
        return chessComparisons()

chessComparisons()