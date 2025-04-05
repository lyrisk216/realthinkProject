#Ceasar encrypt
def encrypt_single_table(txt, key):
    txt2 = ''
    for c in txt:
        if 'A' <= c <= 'Z':
            c2 = key[ord(c) - ord('A')] 
        else:
            c2 = c
        txt2 += c2
    return txt2

def decrypt_single_table(txt, key):
    txt2 = ''
    for c in txt:
        if 'A' <= c <= 'Z':
            c2 = chr(key.index(c) + ord('A'))
        else:
            c2 = c
        txt2 += c2
    return txt2

def encrypt_caesar(txt, key):
    txt2 = ''
    for c in txt:
        if 'A' <= c <= 'Z':
            c2 = chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        else:
            c2 = c
        txt2 += c2
    return txt2

def decrypt_caesar(txt, key):
    txt2 = ''
    for c in txt:
        if 'A' <= c <= 'Z':
            c2 = chr((ord(c) + ord('A') - key) % 26 + ord('A'))
        else:
            c2 = c
        txt2 += c2
    return txt2
# --- main ---
f = open('key1.txt', 'r')
key = f.read()
f.close()
print(key)

f = open('decrypt.in', 'r')
txt = f.read()
f.close()
print(txt)
txt = txt.upper()
print(txt)
##txt2 = encrypt_single_table(txt, key)
##print(txt2)

txt3 = decrypt_single_table(txt, key)
print(txt3)
f = open('decrypt.out', 'w')
f.write(txt)
f.close()
            
