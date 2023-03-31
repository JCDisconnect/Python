import re

puzzle_input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

cratePositions = []
reversed_instructions = []

def print_crateMap():
    for i in range(len(cratePositions)):
        print(i+1, " ", cratePositions[i])

def parse_instruction(line):
    result = re.findall('[0-9]+',line)
    return { 
        "move" : int(result[0]),
        "from" : int(result[1]),
        "to" : int(result[2])
        }

def parse_input(input):
    crateZone = 0
    crateZoneString = ""
    for line in reversed(input.splitlines()):
        if len(line) != 0 and crateZone == 0:
            reversed_instructions.append(line)
        elif len(line) != 0:
            crateZoneString += line + "\n"
        else:
            crateZone += 1
    crateZoneArea = crateZoneString.splitlines()
    for c in crateZoneArea[0]:
        if c.isdigit():
            cratePositions.append(list())

    
    i = 1
    while i < len(crateZoneArea):
        line = crateZoneArea[i]
        cratePositionCounter = 0
        crates = line.split(' ')
        x = 0
        while x < len(crates):
            if crates[x] != "":
                cratePositions[cratePositionCounter].append(crates[x])
                cratePositionCounter += 1
                x += 1
            else:
                cratePositionCounter += 1
                x += 4
        i += 1

def solve_part1():
    for instructionString in reversed(reversed_instructions):
        instructionDict = parse_instruction(instructionString)
        i = 0
        while i < instructionDict["move"]:
            cratePositions[instructionDict["to"]-1].append(cratePositions[instructionDict["from"]-1].pop())
            i+=1

def solve_part2():
    for instructionString in reversed(reversed_instructions):
        instructionDict = parse_instruction(instructionString)
        i = 0
        crateStack = []
        while i < instructionDict["move"]:
            crateStack.append(cratePositions[instructionDict["from"]-1].pop())
            i+=1
        crateStack.reverse()
        for crate in crateStack:
            cratePositions[instructionDict["to"]-1].append(crate)

parse_input(puzzle_input)
solve_part2()
print_crateMap()
####printing resulting code#####
solution = ""
for crateStack in cratePositions:
    solution += crateStack.pop().strip('[').strip(']')
print(solution)