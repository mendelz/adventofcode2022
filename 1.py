with open("1.input", 'r') as elfdata:
    a = elfdata.readlines()

elfbucket = []
new_elf = 0
for thing in a:
    nonewline = thing.strip()
    print(nonewline)
    if nonewline == "":
        elfbucket.append(new_elf)
        new_elf = 0
        print("NEW ELF")
    else:
        new_elf += int(nonewline)

print(sorted(elfbucket))