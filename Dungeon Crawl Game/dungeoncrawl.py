import random

def generateSeed():
    count = 0
    seed = ""
    while count < 10:
        seed += str(random.randint(0,9))
        count += 1

    return seed

def generateMap(difficulty, size):
    mapFile = open("map.txt", "w")
    gridList = []
    rowList = []
    count = 0
    rowCount = 0
    lineString = ""
    mapSize = size

    if difficulty == 0:
        totalEnemies = 0
    elif difficulty == 1:
        totalEnemies = int(1/12 * mapSize)
    elif difficulty == 2:
        totalEnemies = int(1/8 * mapSize)

    while rowCount < mapSize:
        while count < mapSize:
            randomNum = random.randint(0,100)
            if randomNum % 8 == 0:
                rowList.append("[#]")
            elif randomNum % 44 == 0:
                rowList.append("[$]")
            else:
                rowList.append("[ ]")
            count += 1
        count = 0
        gridList.append(rowList[:])
        rowList = []
        rowCount += 1
    rowCount = 0
    count = 0

    gridList[mapSize//2][0] = "[O]"
    exitRow = random.randint(0,mapSize)
    while exitRow == mapSize//2:
        exitRow = random.randint(0,mapSize-1)
    exitColumn = random.randint(1,mapSize-1)
    gridList[exitRow][exitColumn] = "[E]"

    topBar = ""
    bottomBar = ""
    while count < mapSize*3:
        topBar += "_"
        bottomBar += "-"
        count += 1
    count = 0

    mapFile.write(bottomBar + "\n")
    mapFile.write("   You are -> O   Obstacles are -> #    Treasure is -> $   Exit is -> E\n")
    mapFile.write(topBar + "\n")

    while rowCount < mapSize:
        while count < mapSize:
            lineString += gridList[rowCount][count]
            count += 1
        mapFile.write(lineString + "\n")
        lineString = ""
        count = 0
        rowCount += 1
    mapFile.write(bottomBar + "\n")
    print("New map created!")
    mapFile.close()
    return gridList

def main():
    command = str(input("Would you like to play on a small, medium, or large map?: "))
    while command != "small" and command != "medium" and command != "large":
        command = input("Map size invalid!\nPlease enter small, medium, or large: ")
    if command == "small":
        size = 13
    elif command == "medium":
        size = 25
    else:
        size = 37
    #seed = generateSeed()
    difficulty = int(input("Would you like to play on difficulty 0, 1, or 2: "))
    while difficulty != 0 and difficulty != 1 and difficulty != 2:
        print("Invalid Difficulty!")
        difficulty = int(input("Would you like to play on difficulty 0, 1, or 2: "))
    gameMap = generateMap(difficulty, size)

    playerHP = 10
    alive = True
    playerPos = [size//2, 0]

    command = input("Where would you like to go (Type Quit to quit): ")
    while command != "QUIT" and command != "Quit" and command != "quit" and alive == True:
        if playerHP == 0:
            alive = False
        else:
            if command == "right" or command == "Right":
                if playerPos[1] == size-1:
                    print("Invalid direction: edge of map")
            elif command == "left" or command == "Left":
                if playerPos[1] == 0:
                    print("Invalid direction: edge of map")
            command = input("Where would you like to go (Type Quit to quit): ")
    print("-------------Game Over!-------------")
    

main()
