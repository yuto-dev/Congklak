def initGame():

    global pool, base

    pool = [7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    base = [0,0]

def playGame():
    
    status = checkGameStat()
    playerNum = 2

    while status == 0:

        if playerNum == 2:
            playerNum = 1
        elif playerNum == 1:
            playerNum = 2

        print("It is player " + playerNum + "'s turn")

def checkGameStat():
    
    flag = 0

    for elements in pool:
        
        if elements == 0:
            flag = 1

    return flag

initGame()
checkGameStat()