def initGame():

    global pool, base

    pool = [7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    base = [0,0]

def b():
    global pool
    pool1 = 2

def checkGameStat():
    
    flag = 0

    for elements in pool:
        
        if elements == 0:
            flag = 1

    return flag

initGame()
checkGameStat()