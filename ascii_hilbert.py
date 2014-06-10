import sys

def getpath(degree, path):
    if degree == 0:
        return path
    path = path.replace('A', '-CF+AFA+FC-')
    path = path.replace('B', '+AF-BFB-FA+')
    path = path.replace('C', 'B')
    return getpath(degree - 1, path)

def drawpath(path):
    x = y = xmax = ymax = 0
    picture = {}     
    picture[x, y] = 1;     
    facing = 1 #begin facing right
    for char in path:
        if char == '-': facing = (facing - 1) % 4 #turn left
        if char == '+': facing = (facing + 1) % 4 #turn right
        if char == 'F': 
            if facing == 1: #right
                picture[x+1, y] = 1
                picture[x+2, y] = 1
                x = x + 2
                if x > xmax: xmax = x
            elif facing == 2: #down
                picture[x, y-1] = 1
                picture[x, y-2] = 1
                y = y - 2     
            elif facing == 3: #left
                picture[x-1, y] = 1
                picture[x-2, y] = 1
                x = x - 2    
            elif facing == 0: #up
                picture[x, y+1] = 1
                picture[x, y+2] = 1
                y = y + 2  
                if y > ymax: ymax = y
    for h in range(0, xmax+1):
        for v in range(0, ymax+1):
            try:
                if picture[h, v] == 1: sys.stdout.write('#')
            except: sys.stdout.write(' '),
        print('')

if __name__ == "__main__":
    if (not len(sys.argv) == 2) or int(sys.argv[1]) < 1:
        print('Enter a positive integer')
        sys.exit(2)
    degree = int(sys.argv[1])
    path = getpath(degree, 'A')
    drawpath(path)
