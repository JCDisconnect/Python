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

caloriesPerElf = {}
calories = 0
elfCounter = 1;
for snack in snackList:
    if snack.isnumeric():
        calories += int(snack)
    else:
        caloriesPerElf[elfCounter] = calories
        calories = 0
        elfCounter += 1

sortedCaloriesPerElf = sorted(caloriesPerElf.items(), key=lambda x:x[1])
print(sortedCaloriesPerElf.pop())