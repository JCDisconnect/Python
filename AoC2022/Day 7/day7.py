puzzle_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def solve_part1():
    dirDict = {}
    path = ""
    for line in puzzle_input.splitlines():
        if line.startswith('$'):
            if "cd" in line:
                if ".." not in line:
                    path += line[5:] + "/"
                else:
                    startDir = path.rfind('/')
                    endDir = path[:startDir].rfind('/')
                    path = path[:endDir] + "/"
        elif line[0] == "d":
            dirDict[path[1:]] = 0
        elif line[0].isnumeric():
            fileName = line.split(' ')[1]
            fileSize = int(line.split(' ')[0])
            key = path[1:]
            if key in dirDict.keys():
                value = dirDict[key]
                dirDict[key] += fileSize
            else:
                dirDict[key] = fileSize

    subDirectories = {}
    for aKey in dirDict.keys():
        aList = []
        dirSize = 0
        for bKey in dirDict.keys():
            if bKey.startswith(aKey):
                aList.append(bKey)
                dirSize += int(dirDict[bKey])
                subDirectories[aKey] = { 
                    "dirs": aList,
                    "size": dirSize
                }

    totalSize = 0
    for key in subDirectories:
        if subDirectories[key]["size"] <= 100000:
            totalSize += int(subDirectories[key]["size"])

    print("Part 1:",totalSize)

def solve_part2():
    dirDict = {}
    path = ""
    for line in puzzle_input.splitlines():
        if line.startswith('$'):
            if "cd" in line:
                if ".." not in line:
                    path += line[5:] + "/"
                else:
                    startDir = path.rfind('/')
                    endDir = path[:startDir].rfind('/')
                    path = path[:endDir] + "/"
        elif line[0].isnumeric():
            fileName = line.split(' ')[1]
            fileSize = int(line.split(' ')[0])
            key = path[1:]
            if key in dirDict.keys():
                value = dirDict[key]
                dirDict[key] += fileSize
            else:
                dirDict[key] = fileSize

    subDirectories = {}
    for aKey in dirDict.keys():
        aList = []
        dirSize = 0
        for bKey in dirDict.keys():
            if bKey.startswith(aKey):
                aList.append(bKey)
                dirSize += int(dirDict[bKey])
                subDirectories[aKey] = { 
                    "dirs": aList,
                    "size": dirSize
                }

    print("-------------")
    totalDiskSpace = 70000000
    updateSize = 30000000
    unusedSpace = totalDiskSpace - subDirectories["/"]["size"]
    requiredSpace = (unusedSpace - updateSize)*-1
    candidatesList = []
    print("Unused Space:",unusedSpace)
    print("Required Space:",(requiredSpace))
    print("-------------")
    print("Candidate List")
    print("-------------")
    totalSize = 0
    for key in subDirectories:
        if subDirectories[key]["size"] >= requiredSpace:
            totalSize += int(subDirectories[key]["size"])
            print(key,subDirectories[key]["size"])
            candidatesList.append(subDirectories[key]["size"])
    candidatesList.sort()
    print("-------------")
    print(candidatesList[0])
    
solve_part2()