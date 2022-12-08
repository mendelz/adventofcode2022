# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8

# Break out line into two ranges
def range_intersection(pair):
    elf1, elf2 = pair.strip().split(',')
    elf1_range = set(range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1))
    elf2_range = list(range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1))
    intersect = elf1_range.intersection(elf2_range)
    if len(intersect) > 0:
        return True
    #if set(intersect) == set(elf1_range) or set(intersect) == set(elf2_range):
    #    return True 
    else: 
        return False

#print(range_intersection("2-8,3-7"))

with open("4.input", 'r') as inputfile:
    lines = inputfile.readlines()

total = 0
for line in lines:
    if range_intersection(line): total += 1 
print(total)