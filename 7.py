with open('7.input', 'r') as inputfile:
    lines = inputfile.read().split('\n')

directory_tree = {}
pwd = ''
for idx, line in enumerate(lines):
    if line[0] == '$':
        if 'cd /' in line:
            directory_tree['/'] = []
            pwd = '/'
        elif line[2:4] == 'cd':
            dest = line[4:]
            if dest.strip() == '..':
                pwd = pwd[:-len(pwd.split('/')[-1])-1]
            else:
                pwd = pwd + dest.strip() if pwd == '/' else pwd + '/' + dest.strip()
        elif line[2:4] == 'ls':
            for output_line in lines[idx+1:]:
                if '$' in output_line:
                    break
                else:
                    if 'dir' in output_line.strip().split()[0]:
                        dir_key = pwd+output_line.strip().split()[1] if pwd == '/' else pwd + '/' + output_line.strip().split()[1]
                        directory_tree[dir_key] = []
                        directory_tree[pwd].append(dir_key)
                    else:
                        directory_tree[pwd].append(int(output_line.split()[0]))
            # print(line[2:10])
            # print(lines[idx-1])

def add_files(dir_dict, dir_spec, running_total=0):
    for idx, thing in enumerate(dir_spec):
        if type(thing) == str:
            dir_spec.pop(idx)
            return add_files(dir_dict, dir_dict[thing] + dir_spec)
        else:
            running_total += thing
    return running_total

pt1 = 0
pt2 = []
total = 0
for key in directory_tree.keys():
    dir_total = add_files(directory_tree, directory_tree[key])
    if key == '/':
        total = dir_total
    if dir_total <= 100000:
        pt1 += dir_total
    pt2.append(dir_total)
print("part 1 {}".format(pt1))

for item in sorted(pt2):
    free = 70000000 - total
    if item+free >= 30000000:
        print(item)
        break

# for key in a.keys():
#     print(add_files(a, a[key]))

# print(add_files(a, a['/dira/dire']))