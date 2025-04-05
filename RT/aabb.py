#aabb
#solution
for n in range(10000):
    n1 = n % 10
    n2 = n // 10 % 10
    n3 = n // 100 % 10
    n4 = n // 1000 % 10
    if n1 == n2 and n3 == n4 and n ** 0.5 % 1 == 0:
        print(n)


for a in range(10):
    for b in range(10):
        n = a * 1100 + b * 11
        if n ** 0.5 % 1 == 0:
            print(n)


for i in range(100):
    n = i * i
    n1 = n % 10
    n2 = n // 10 % 10
    n3 = n // 100 % 10
    n4 = n // 1000 % 10
    if n1 == n2 and n3 == n4:
        print(n)
    
            
