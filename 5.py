#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


mapping = {1:1, 5:2, 9:3, 13:4, 17:5, 21:6, 25:7, 29:8, 33:9}

import math
from collections import defaultdict
def get_starting_state(stack_string):
    lines = stack_string.split('\n')
    lines.reverse()
    # find the number of stacks by dividing by 4 and rounding up
    stack_count = math.ceil(len(lines[0])/4)
    stacks = defaultdict(list)
    for line in lines:
        # bucket size is 4
        for item in line:
            if item != '.' and item != '':
                try:
                    int(item)
                except ValueError:
                    stacks[mapping[line.index(item)]].append(item)
                    templist = list(line)
                    templist[line.index(item)] = '.'
                    line = ''.join(templist)

    return stacks                

def parse_instruction(instruction):
    try:
        number_to_move = int(instruction[5:7])
        start_stack = int(instruction[13])
        dest_stack = int(instruction[18])
    except ValueError:
        number_to_move = int(instruction[5])
        start_stack = int(instruction[12])
        dest_stack = int(instruction[17])
    return number_to_move, start_stack, dest_stack

def run_crane(number_to_move, start_stack, dest_stack, stacks):
    crane = []
    for crates in range(number_to_move):
        crane.append(stacks[start_stack].pop())
    for crates in range(number_to_move):
        stacks[dest_stack].append(crane.pop())

with open('5.input', 'r') as input:
    data = input.read()

stack_string = data.split('move')[0].replace(" ", ".").replace("[", ".").replace("]", ".")
lines = data.split('\n')
instructions = []
for line in lines:
    if 'move' in line:
        instructions.append(line)

stacks = get_starting_state(stack_string)
for instruction in instructions:
    number_to_move, start_stack, dest_stack = parse_instruction(instruction)
    run_crane(number_to_move, start_stack, dest_stack, stacks)

print(stacks)