# Vigenere Cipher
def index(char):
    if char.islower():
        return ord(char) - ord('a')
    else:
        return ord(char) - ord('A')

def adjustkey(key,plainLen):
    keyLen = len(key)
    return ''.join(key[x % keyLen] for x in range(plainLen))

def encrypt(plaintxt,key):
    plainLen = len(plaintxt)
    key = adjustkey(key,plainLen)
    ciphertxt = ''
    j = 0
    for i in range(plainLen):
        if plaintxt[i].islower():
            ciphertxt += chr((index(plaintxt[i]) + index(key[j].lower())) % 26 + ord('a'))
            j += 1
        elif plaintxt[i].isupper():
            ciphertxt += chr((index(plaintxt[i]) + index(key[j].upper())) % 26 + ord('A'))
            j += 1
        else:
            ciphertxt += plaintxt[i]
    return ciphertxt

def decrypt(ciphertxt,key):
    cipherLen = len(ciphertxt)
    key = adjustkey(key,cipherLen)
    plaintxt = ''
    j = 0
    for i in range(cipherLen):
        if ciphertxt[i].islower():
            plaintxt += chr(ord('a') + (ord(ciphertxt[i]) - ord(key[j].lower())) % 26)
            j += 1
        elif ciphertxt[i].isupper():
            plaintxt += chr(ord('A') + (ord(ciphertxt[i]) - ord(key[i].upper())) % 26)
            j += 1
        else:
            plaintxt += ciphertxt[i]
    return plaintxt
