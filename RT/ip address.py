#ip address
ipList = eval(input('ip address:'))
for i in range(4):
    print(ipList[i])


a = ('00000000' + bin(ipList[0])[2:])[-8:]
b = ('00000000' + bin(ipList[1])[2:])[-8:]
c = ('00000000' + bin(ipList[2])[2:])[-8:]
d = ('00000000' + bin(ipList[3])[2:])[-8:]
print(int(a + b + c + d, 2))
print(a)



#2
print(ipList[0] * 256 ** 3 + ipList[1] * 256 ** 2 + ipList[2] * 256 ** 1 + ipList[3])


#3
print(ipList[0] * pow(256, 3) + ipList[1] * pow(256, 2) + ipList[2] * pow(256, 1) + ipList[3])


#192, 168, 1, 177
