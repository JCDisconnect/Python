"""
https://adventofcode.com/2022/day/2
Win the Rock Paper Scissor Tournament by cheating
"""
elfCheatSheet = """A Y
B X
C Z"""

cheatSheetInterpreterPart1 = {
    'A' : 'Rock', 
    'B' : 'Paper',
    'C' : 'Scissor',
    'X' : 'Rock',
    'Y' : 'Paper',
    'Z' : 'Scissor'
    }

cheatSheetInterpreterPart2 = {
    'X' : 'Loss',
    'Y' : 'Draw',
    'Z' : 'Victory'
    }

valuePerChoice = {'Rock': 1, 'Paper': 2, 'Scissor' : 3}
valuePerResult = {'Loss' : 0, 'Draw' : 3, 'Victory' : 6}

resultPerMatchup = {
    'Rock Scissor' : 'Victory',
    'Scissor Paper' : 'Victory',
    'Paper Rock' : 'Victory',
    'Scissor Rock' : 'Loss',
    'Paper Scissor' : 'Loss',
    'Rock Paper' : 'Loss',
    'Paper Paper' : 'Draw',
    'Rock Rock' : 'Draw',
    'Scissor Scissor' : 'Draw'
    }

strategyMap = {
    'Victory' : { 
        'Scissor' : 'Rock',
        'Paper' : 'Scissor',
        'Rock' : 'Paper'
    },
    'Draw' : {
        'Scissor' : 'Scissor',
        'Paper' : 'Paper',
        'Rock' : 'Rock'
    },
    'Loss' : {
        'Rock' : 'Scissor',
        'Scissor' : 'Paper',
        'Paper' : 'Rock'
    }
}

def solve_part1():
    totalPoints = 0
    for line in elfCheatSheet.splitlines():
        opponentChoice = cheatSheetInterpreterPart1[line.split()[0]]
        playerChoice = cheatSheetInterpreterPart1[line.split()[1]]
        totalPoints += valuePerChoice[playerChoice] + valuePerResult[resultPerMatchup[playerChoice + ' ' + opponentChoice]]
    print(totalPoints)

def solve_part2():
    totalPoints = 0
    for line in elfCheatSheet.splitlines():
        opponentChoice = cheatSheetInterpreterPart1[line.split()[0]]
        strategyChoice = strategyMap[cheatSheetInterpreterPart2[line.split()[1]]]
        playerChoice = strategyChoice[opponentChoice]
        totalPoints += valuePerChoice[playerChoice] + valuePerResult[resultPerMatchup[playerChoice + ' ' + opponentChoice]]
    print(totalPoints)    

solve_part1()
solve_part2()