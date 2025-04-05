#ACSL20-21R1
def add_digits(n):      
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
def add_to_one(n):
    while True:
        n = add_digits(n)
        if n < 10:
            return n
#---main---
s, d, r = eval(input('start, delta, rows = '))
for y in range(r):
    rowSum = 0
    for x in range(y + 1):
        s = add_to_one(s)
        print(s, end = ' ')
        rowSum += s
        s += d
    print()
print(rowSum)

#最后出循环才打印
#增加一个变量rowSum
#每次行循环开始把rowSum清零， 最后保留下来的就是最后一行的和
