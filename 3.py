# pt1
def solve(sack):
    common_type = list(set(sack[int(len(sack)/2):]).intersection(sack[:int(len(sack)/2)]))
    return ord(common_type[0]) - 38 if common_type[0].isupper() else ord(common_type[0]) - 96

with open("3.input", 'r') as f:
    input_lines = f.readlines()

total = 0
for line in input_lines:
    total += solve(line)

print("solution 1: {}".format(total))


# pt 2
import numpy as np

def solve_group(group_of_sacks):
    # find the badges
    badges = list(set(group_of_sacks[0].strip()).intersection(group_of_sacks[1].strip(), group_of_sacks[2].strip()))
    return ord(badges[0]) - 38 if badges[0].isupper() else ord(badges[0]) - 96

total = 0
groups = np.array_split(input_lines, int(len(input_lines)/3))
for group in groups:
    total += solve_group(group)

print("solution 2: {}".format(total))