import sys, fileinput
lines = [int(line.strip()) for line in fileinput.input(files=sys.argv[1])]

window = []

for i,_ in enumerate(lines):
    window_sum = sum(lines[i-2:i+1])
    if window_sum > 0:
        window.append(window_sum)

count = 0
for i,num in enumerate(window):
    if num > window[i-1]:
        count+=1
    
print(count)