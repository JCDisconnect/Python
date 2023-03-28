"""
https://adventofcode.com/2022/day/1
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
snacksString = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

snackList = snacksString.splitlines()

def solve_puzzle(puzzle_input):
    caloriesPerElf = {}
    calories = 0
    elfCounter = 1
    for snack in snackList:
        if snack.isnumeric():
            calories += int(snack)
        else:
            caloriesPerElf[elfCounter] = calories
            calories = 0
            elfCounter += 1
    #Sort list by values to get the largest value first because I'm a lazy elf
    return sorted(caloriesPerElf.items(), key=lambda x:x[1])

def solve_part1(puzzle_input):
    sortedCaloriesPerElf = solve_puzzle(puzzle_input)
    print("Part 1:",sortedCaloriesPerElf.pop()[1])
    
def solve_part2(puzzle_input):
    sortedCaloriesPerElf = solve_puzzle(puzzle_input)
    sumTopThreeCalories = 0
    for i in range(3):
        sumTopThreeCalories += sortedCaloriesPerElf.pop()[1]
    print("Part 2:", sumTopThreeCalories)

solve_part1(snackList)
solve_part2(snackList)