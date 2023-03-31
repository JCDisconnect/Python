puzzle_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

elfPairs = {}

def fully_contains(range1,range2):
    firstFrom = int(range1.split('-')[0])
    firstTo = int(range1.split('-')[1])
    secondFrom = int(range2.split('-')[0])
    secondTo = int(range2.split('-')[1])
    if firstFrom >= secondFrom and firstTo <= secondTo:
        return True
    if secondFrom >= firstFrom and secondTo <= firstTo:
        return True
    else:
        return False

def get_overlaps(range1,range2):
    firstFrom = int(range1.split('-')[0])
    firstTo = int(range1.split('-')[1])
    secondFrom = int(range2.split('-')[0])
    secondTo = int(range2.split('-')[1])
    if firstFrom <= secondFrom and firstTo >= secondFrom:
        return True
    if secondFrom <= firstFrom and secondTo >= firstFrom:
        return True

def solve_part1_2(input):
    pairCounter1 = 0
    pairCounter2 = 0
    for line in input.splitlines():
        if fully_contains(line.split(',')[0],line.split(',')[1]) == True:
            pairCounter1 += 1
        if get_overlaps(line.split(',')[0],line.split(',')[1]) == True:
            pairCounter2 += 1
    print('P1:', pairCounter1)
    print('P2:', pairCounter2)

solve_part1_2(puzzle_input)

