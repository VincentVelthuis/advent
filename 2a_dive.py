import sys, fileinput

coord = [0,0]

def change_loc(dir,dist):
    global coord
    if dir == 'forward':
        coord[0] += dist
    elif dir == 'down':
        coord[1] += dist
    elif dir == 'up':
        coord[1] -= dist

# take actions
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

for line in lines:
    direction,distance = line.split(" ")
    change_loc(direction, int(distance))
    # print(coord)
    
ans = coord[0]*coord[1]
print(coord,"-->",ans)

