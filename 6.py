def scan(code):
    scanner = []
    for idx, char in enumerate(code):
        if len(scanner) == 14:
            # get rid of first
            scanner.pop(0)
            # append new one
            scanner.append(char)
            # are all 4 different?
            if len(set(scanner)) == 14:
                return idx
            else:
                continue
        else:
            scanner.append(char)


with open('6.input', 'r') as input:
    code = input.read()

print(scan(code)+1)