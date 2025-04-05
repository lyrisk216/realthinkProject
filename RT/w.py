import random
while True:
    s, n = eval(input('随机红包总金额，人数：'))
    if s >= n*0.01:#金额够分，则跳出循环
        break
    print('金额太少不够分，请重新输入！')
mList = [1] * n#初始化
cents = int(s * 100 - n)#需要做随机处理的总金额，单位：分
for i in range(n - 1):
    r = random.randint(0, int(cents / (n - i)) * 2)
    mList[i] += r
    cents -= r
mList[n - 1] += cents#最后一个人，不需要再随机
for i in range(n):
    print(mList[i] / 100)#打印时恢复单位：元
