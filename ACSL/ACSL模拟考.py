txtbook = input()
mima = input()
mimachuan = mima.split(" ")

for i in range(len(mimachuan)):
    s = int(mimachuan[i].split(".")[0])
    w = int(mimachuan[i].split(".")[1])
    c = int(mimachuan[i].split(".")[2])
    #print(s,w,c)

    try:
        letter = txtbook.split("  ")[s-1].split(" ")[w-1][c-1]
    except:
        letter = " "

    print(letter, end='')
    









