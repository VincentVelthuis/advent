import sys, fileinput

coord = [0,0,0] # [horizontal,depth,aim]

def change_loc(dir,x):
    global coord
    if dir == 'forward':
        # forward X increases your horizontal position by X units.
        coord[0] += x
        # forward X increases your depth by your aim multiplied by X.
        coord[1] += coord[2] * x
    elif dir == 'down':
        # down X increases your aim by X units.
        coord[2] += x
    elif dir == 'up':
        # up X decreases your aim by X units.
        coord[2] -= x

# take actions
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

for line in lines:
    direction,distance = line.split(" ")
    change_loc(direction, int(distance))
    
ans = coord[0]*coord[1]
print(coord,"-->",ans)

