import numpy as np

puzzle_input_test ="""30373
25512
65332
33549
35390"""

def getVisibility(start,trees):
    xLimit = trees.shape[0]
    yLimit = trees.shape[1]
    xStart = start[0]
    yStart = start[1]
    topScore = 0
    bottomScore = 0
    leftScore = 0
    rightScore = 0
    startTree = trees[xStart,yStart]
    returnDict = {
        "ScenicScore" : 1,
        "Directions" : {
            "Top" : True,
            "Bottom" : True,
            "Left" : True,
            "Right" : True,
            }
        }

    #Top
    # print("Top")
    if yStart > 0:
        i = yStart-1
        while i >= 0:
            tree = trees[xStart,i]
            # print(tree)
            topScore += 1
            if tree >= startTree:
                returnDict["Directions"]["Top"] = False
                break
            i -= 1
    else:
        returnDict["Directions"]["Top"] = True
    #Bottom
    # print("Bottom")
    if yStart < yLimit-1:
        i = 1
        while i+yStart < yLimit:
            tree = trees[xStart,yStart+i]
            # print(tree)
            bottomScore += 1
            if tree >= startTree:
                returnDict["Directions"]["Bottom"] = False
                break
            i += 1
    else:
        returnDict["Directions"]["Bottom"] = True
    #Left
    # print("Left")
    if xStart > 0:
        i = xStart-1
        while i >= 0:
            tree = trees[i,yStart]
            # print(tree)
            leftScore += 1
            if tree >= startTree:
                returnDict["Directions"]["Left"] = False
                break
            i -= 1
    else:
        returnDict["Directions"]["Left"] = True
    #Right
    # print("Right")
    if xStart < xLimit-1:
        i = 1
        while i+xStart < xLimit:
            tree = trees[xStart+i,yStart]
            # print(tree)
            rightScore += 1
            if tree >= startTree:
                returnDict["Directions"]["Right"] = False
                break
            i += 1
    else:
        returnDict["Directions"]["Right"] = True
    returnDict["ScenicScore"] = leftScore * rightScore * topScore * bottomScore
    return returnDict

def generate_tree_map(inputStr):
    inputList = inputStr.splitlines()
    yDimension = len(inputList)
    xDimension = len(inputList[0])
    treeMap = np.zeros([xDimension,yDimension])
    x = 0
    y = 0
    for line in inputList:
        x = 0
        for c in line:
            treeMap[x,y] = int(c)
            x += 1
        y += 1
    return treeMap

def getVisibleTrees(treeMapInput):
    treeMap = generate_tree_map(treeMapInput)
    xDimension = treeMap.shape[0]
    yDimension = treeMap.shape[1]
    visibleTrees = 0
    scenicHighScore = 0
    for x in range(xDimension):
        for y in range(yDimension):
            tree = getVisibility((x,y),treeMap)
            if tree["ScenicScore"] > scenicHighScore:
                scenicHighScore = tree["ScenicScore"]
            for direction in tree["Directions"].keys():
                if tree["Directions"][direction] == True:
                    visibleTrees += 1
                    break
    print("Visible Trees:",visibleTrees)
    print("Scenic Highscore:",scenicHighScore)

def solve_part1(treeMapInput):
    getVisibleTrees(treeMapInput)

def test_Example_Input_Visibility():
    """
    30373
    25512
    65332
    33549
    35390
    """
    treeMap = generate_tree_map(puzzle_input_test)
    #The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    topLeft5 = getVisibility((1,1),treeMap) 
    if topLeft5["Directions"]["Left"] == True and topLeft5["Directions"]["Top"] == True:
        if topLeft5["Directions"]["Right"] == False and topLeft5["Directions"]["Bottom"] == False:
            print("Test 1 Success")
    
    #The top-middle 5 is visible from the top and right.
    topMiddle5 = getVisibility((2,1),treeMap)
    if topMiddle5["Directions"]["Top"] == True and topMiddle5["Directions"]["Right"] == True:
        if topMiddle5["Directions"]["Left"] == False and topMiddle5["Directions"]["Bottom"] == False:
            print("Test 2 Success")
    
    #The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    topRight1 = getVisibility((3,1),treeMap)
    if topRight1["Directions"]["Top"] == False and topRight1["Directions"]["Bottom"] == False:
        if topRight1["Directions"]["Left"] == False and topRight1["Directions"]["Right"] == False:
            print("Test 3 Success")
    
    #The left-middle 5 is visible, but only from the right.
    leftMiddle5 = getVisibility((1,2),treeMap)
    if leftMiddle5["Directions"]["Right"] == True:
        if leftMiddle5["Directions"]["Left"] == False and leftMiddle5["Directions"]["Top"] == False and leftMiddle5["Directions"]["Bottom"] == False:
            print("Test 4 Success")
    
    #The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    center3 = getVisibility((2,2),treeMap)
    if center3["Directions"]["Left"] == False and center3["Directions"]["Right"] == False and center3["Directions"]["Top"] == False and center3["Directions"]["Bottom"] == False:
        print("Test 5 Success")
    
    #The right-middle 3 is visible from the right.
    rightMiddle3 = getVisibility((3,2),treeMap)
    if rightMiddle3["Directions"]["Right"] == True and rightMiddle3["Directions"]["Left"] == False and rightMiddle3["Directions"]["Top"] == False and rightMiddle3["Directions"]["Bottom"] == False:
        print("Test 6 success")
    #In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
    bottom3Flag = True
    bottom4Flag = True
    bottom5Flag = True

    bottom4 = getVisibility((3,3),treeMap)
    bottom3 = getVisibility((1,3),treeMap)
    bottom5 = getVisibility((2,3),treeMap)

    if bottom5["Directions"]["Top"] == False and bottom5["Directions"]["Left"] == True and bottom5["Directions"]["Right"] == False and bottom5["Directions"]["Bottom"] == True:
        bottom5Flag = True
    for key in bottom3["Directions"].keys():
        if bottom3["Directions"][key] == True:
            bottom3Flag = False
    for key in bottom4["Directions"].keys():
        if bottom4["Directions"][key] == True:
            bottom4Flag = False
    if (bottom3Flag & bottom4Flag & bottom5Flag) == True:
        print("Test 7 success")
    getVisibleTrees(puzzle_input_test)

    if topMiddle5["ScenicScore"] == 4:
        print("Scenic Test 1 Success")
    
    if bottom5["ScenicScore"] == 8:
        print("Scenic Test 2 Success")

test_Example_Input_Visibility()
