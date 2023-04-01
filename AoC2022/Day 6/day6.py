puzzle_example_list = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb","bvwbjplbgvbhsrlpgdmjqwftvncz","nppdvjthqldpwncqszvftbrmjlhg","nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg","zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
puzzle_input ="mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def find_sequence_start(input,length):
    counter = 0
    i = 0
    while i < int(len(input)):
        seed = input[i]
        slice = input[i+1:i+length-counter]
        if seed not in slice:
            counter += 1
            if counter == length:
                print(i+1)
                # print(input[i-length+1:i+1])
                break
        else:
            counter = 0
        i += 1

find_sequence_start(puzzle_input,14)

# #part 1
# print("Part 1:")     
# for input in puzzle_example_list:
#      print(input)
#      find_sequence_start(input,4)
# #part 2
# print("Part 2:")
# for input in puzzle_example_list:
#      print(input)
#      find_sequence_start(input,14)