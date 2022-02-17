import sys, fileinput
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

count = 0

for index,item in enumerate(lines[1:]):
    if item > lines[index]:
        count += 1
    elif item == lines[index]: 
        print(item, lines[index])

print(count)