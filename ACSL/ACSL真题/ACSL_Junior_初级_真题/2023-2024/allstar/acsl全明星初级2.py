g = input().split()
grid = []
fnd = []
g[0],g[1]=int(g[0]),int(g[1])
w = input()
fw = input().split()
def fnd2(x,y,f):
    if x >= len(f)-1:
        if y >= len(f)-1:
            w = ''
            for i in range(len(f)):
                w += grid[x-i][y-i]
            if w == f:
                for i in range(len(f)):
                    fnd[x-i][y-i] = 1
                return
        w = ''
        for i in range(len(f)):
            w += grid[x-i][y]
        if w == f:
            for i in range(len(f)):
                fnd[x-i][y]=1
            return
        if y <= g[1]-len(f):
            w = ''
            for i in range(len(f)):
                w += grid[x-i][y+i]
            if w == f:
                for i in range(len(f)):
                    fnd[x-i][y+i]=1
                return
    if x <= g[0]-len(f):
        if y >= len(f)-1:
            w = ''
            for i in range(len(f)):
                w += grid[x+i][y-i]
            if w == f:
                for i in range(len(f)):
                    fnd[x+i][y-i] = 1
                return
        w = ''
        for i in range(len(f)):
            w += grid[x+i][y]
        if w == f:
            for i in range(len(f)):
                fnd[x+i][y]=1
            return
        if y <= g[1]-len(f):
            w = ''
            for i in range(len(f)):
                w += grid[x+i][y+i]
            if w == f:
                for i in range(len(f)):
                    fnd[x+i][y+i]=1
                return
    if y>=len(f)-1:
        w = ''
        for i in range(len(f)):
            w += grid[x][y-i]
        if w == f:
            for i in range(len(f)):
                fnd[x][y-i]=1
            return
    if y <= g[1]-len(f):
        w = ''
        for i in range(len(f)):
            w += grid[x][y+i]
        if w == f:
            for i in range(len(f)):
                fnd[x][y+i] = 1
            return
    return
for i in range(g[0]):
    fnd.append([])
    grid.append(w[i*g[1]:i*g[1]+g[1]])
    for j in range(g[1]):
        fnd[-1].append(0)
for f in fw:
    for x in range(g[0]):
        for y in range(g[1]):
            if grid[x][y] == f[0]:
                fnd2(x,y,f)
w = ''
for x in range(len(fnd)):
    for y in range(len(fnd[0])):
        if fnd[x][y] == 0:
            w += grid[x][y]
print(w)
