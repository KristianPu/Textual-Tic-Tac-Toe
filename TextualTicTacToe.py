lista = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
dictOX = {x:y for x,y in enumerate(lista)}
#print(dictOX)


def PlayerO():
    
    while True:
        try:
            Placeit = int(input("Where would you like to add O (1-9): "))
            if dictOX[Placeit].isspace():
                Insert("O", Placeit)
                break
            else:
                print("This place is taken, please try again!")
                PlayerO()

        except:
            print("Wrong input, try a number between 1 and 9.")
            PlayerO()


def PlayerX():
    
    while True:
        try:
            Placeit = int(input("Where would you like to add X (1-9): "))
            if dictOX[Placeit].isspace():
                Insert("X", Placeit)
                break
            else:
                print("This place is taken, please try again!")
                PlayerX()

        except:
            print("Wrong input, try a number between 1 and 9.")
            PlayerX()


def PrintBox():
    print(" " + dictOX[1] + " " + "|" + " " + dictOX[2] + " " + "|" + " " + dictOX[3] + " ")
    print("---" + "|" + "---" + "|" + "---")
    print(" " + dictOX[4] + " " + "|" + " " + dictOX[5] + " " + "|" + " " + dictOX[6] + " ")
    print("---" + "|" + "---" + "|" + "---")
    print(" " + dictOX[7] + " " + "|" + " " + dictOX[8] + " " + "|" + " " + dictOX[9] + " ")


def Insert(XO, Place):
    dictOX[Place] = XO
    PrintBox()
    CheckWinner(XO)


def CheckWinner(XO):

    from collections import Counter

    counter = Counter[dictOX.values()]
    winner = False

    if dictOX[1] == XO and dictOX[2] == XO and dictOX[3] == XO or dictOX[4] == XO and dictOX[5] == XO and dictOX[6] == XO or dictOX[7] == XO and dictOX[8] == XO and dictOX[9] == XO or dictOX[1] == XO and dictOX[4] == XO and dictOX[7] == XO or dictOX[2] == XO and dictOX[5] == XO and dictOX[8] == XO or dictOX[3] == XO and dictOX[6] == XO and dictOX[9] == XO or dictOX[1] == XO and dictOX[5] == XO and dictOX[9] == XO or dictOX[3] == XO and dictOX[5] == XO and dictOX[7] == XO:
        
        if XO == "X":
            print("Congratulations Player X won!")
            winner = True

        elif XO == "O":
            print("Congratulations Player O won!")
            winner = True
            

    elif sum(1 for i in dictOX if dictOX[i].isspace()) > 1 and winner == False:

        if XO == "X":
            PlayerO()
        else:
            PlayerX()


PrintBox()
CheckWinner(0)
