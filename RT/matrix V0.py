#matrix V0
def matrix_show(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            print(m[y][x], end = '\t')
        print()
    return
#--- main ---
w, h = eval(input('w, h = '))
matrix = []
for y in range(h):
    matrix.append( [0] * w )
for y in range(h):
    for x in range(w):
        matrix[y][x] = y * w + x
while True:
    matrix_show(matrix)
    x1, y1, vx, vy = eval(input('x1, y1, vx, vy = '))
    if not ([vx, vy] in [ [0, -1], [0, 1], [-1, 0], [1, 0] ]):
        print('Illegal input!')
    x2, y2 = x1 + vx, y1 + vy
    if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h:
        print('Out of range!')
        continue
    matrix[y1][x1], matrix[y2][x2] = \
                    matrix[y2][x2], matrix[y1][x1]
