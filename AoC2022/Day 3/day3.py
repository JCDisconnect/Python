import string

puzzle_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

priorityDict = {}
rucksacksDict = {}
rucksackListPart1 = []
elfGroupListPart2 = []

class elfGroupClass:
    firstElf = None
    secondElf = None
    thirdElf = None
    groupBadge = ""
    groupBadgeValue = 0
    def __init__(self, rucksacks):
        rucksackList = rucksacks.splitlines()
        self.firstElf = rucksackClass(rucksackList[0])
        self.secondElf = rucksackClass(rucksackList[1])
        self.thirdElf = rucksackClass(rucksackList[2])
        self.__setGroupBadge()
    def __setGroupBadge(self):
        firstRucksack = self.firstElf.compartment1 + self.firstElf.compartment2
        secondRucksack = self.secondElf.compartment1 + self.secondElf.compartment2
        thirdRucksack = self.thirdElf.compartment1 + self.thirdElf.compartment2
        for c1 in firstRucksack:
            for c2 in secondRucksack:
                for c3 in thirdRucksack:
                    if c1 == c2 == c3:
                        self.groupBadge = c1
                        self.groupBadgeValue = priorityDict[c1]
                        return

class rucksackClass:
    priorityValue = 0
    rucksackSize = 0
    compartment1 = ""
    compartment2 = ""
    priorityItems = ""

    def __init__(self, rucksack):
        self.rucksackSize = len(rucksack)
        self.compartment1 = (rucksack[:int((self.rucksackSize/2))])
        self.compartment2 = (rucksack[int((self.rucksackSize/2)):])
        self.__setPriorityItems()
        for p in self.priorityItems:
            self.priorityValue += priorityDict[p]   

    def __setPriorityItems(self):
        duplicateItems = set()
        for c1 in self.compartment1:
            for c2 in self.compartment2:
                if c1 == c2:
                    duplicateItems.add(c1)
        self.priorityItems = duplicateItems

def createRucksacks(rucksacks):
    rucksackList = []
    for rLine in rucksacks.splitlines():
        rucksack = rucksackClass(rLine)
        rucksackList.append(rucksack)
    return rucksackList

def createPriorityLookup():
    priorityCounter = 1
    for c in string.ascii_lowercase:
        priorityDict[c] = priorityCounter
        priorityCounter += 1
    for c in string.ascii_uppercase:
        priorityDict[c] = priorityCounter
        priorityCounter += 1

def solve_part1():
    rucksackListPart1 = createRucksacks(puzzle_input)
    prioritySum = 0
    for r in rucksackListPart1:
        prioritySum += r.priorityValue
    print('Part1:', prioritySum)

def solve_part2():
    rucksackList = puzzle_input.splitlines()
    rucksacksGroup = ""
    for i in range(len(rucksackList)):
        rucksacksGroup += rucksackList[i] + '\n'
        if (i+1)%3 == 0:
            elfGroup = elfGroupClass(rucksacksGroup)
            elfGroupListPart2.append(elfGroup)
            rucksacksGroup = ""

    elfGroupBadgeSum = 0
    for elfGroup in elfGroupListPart2:
        elfGroupBadgeSum += elfGroup.groupBadgeValue
    print("Part2:",elfGroupBadgeSum)
    
createPriorityLookup()
solve_part1()
solve_part2()