#prime neibour
diff = list()
a = eval(input('input numbers = '))
for i in range(1, len(a)):
    diff.append(a[i] - a[i - 1])
print(diff)
    
    
    
