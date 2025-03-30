#嵌套矩阵
a = eval(input('a = '))
n = 2 * a - 1
matrix = []
for y in range(n):
    matrix.append([0] * n)
#----
##for y in range(a):
##    for x in range(y, a):
##        matrix[y][x] = a - y
##        matrix[x][y] = matrix[y][x]
##for y in range(a):
##    for x in range(a):
##        matrix[y][n - 1 - x] = matrix[y][x]
##for y in range(a):
##    for x in range(n):
##        matrix[n - 1 - y][x] = matrix[y][x]

##x0, y0 = a - 1, a - 1
##for y in range(n):
##    for x in range(n):
##        matrix[y][x] = max(abs(x - x0), abs(y - y0)) + 1

#正方形
for i in range(a):
    for y in range(i, n - i):
        for x in range(i, n - i):
            matrix[y][x] = a - i
        
#----
for y in range(n):
    for x in range(n):
        print(matrix[y][x], end = ' ')
    print()
