
def show_matrix(m):
    for line in m:
        print(line)
def rotate_clockwise(m):
    n = len(m)
    nm = []
    for y in range(n):
        nm.append( [0] * n)
    for y in range(n):
        for x in range(n):
            nm[x][n - 1 - y] = mList[y][x]
    return nm
#-- main --
mList = []
n = 5
for y in range(n):
    line = []
    for x in range(n):
        line.append(y * n + x)
    mList.append(line)
print(mList)
show_matrix(mList)

nm = []
m2 = rotate_clockwise(mList)
show_matrix(m2)
