# Vigenere Cipher
def adjustkey(key,plainLen):
    keyLen = len(key)
    return ''.join(key[x % keyLen] for x in range(plainLen))

def encrypt(plaintxt,key):
    plainLen = len(plaintxt)
    key = adjustkey(key,plainLen)
    ciphertxt = ''
    for i in range(plainLen):
        if plaintxt[i].islower():
            ciphertxt += chr((ord(plaintxt[i]) + ord(key[i].lower()) - 2*ord('a')) % 26 + ord('a'))
        elif plaintxt[i].isupper():
            ciphertxt += chr((ord(plaintxt[i]) + ord(key[i].upper()) - 2*ord('A')) % 26 + ord('A'))
        else:
            ciphertxt += plaintxt[i]
    return ciphertxt

def decrypt(ciphertxt,key):
    cipherLen = len(ciphertxt)
    key = adjustkey(key,cipherLen)
    plaintxt = ''
    for i in range(cipherLen):
        if ciphertxt[i].islower():
            plaintxt += chr(ord('a') + (ord(ciphertxt[i]) - ord(key[i].lower())) % 26)
        elif ciphertxt[i].isupper():
            plaintxt += chr(ord('A') + (ord(ciphertxt[i]) - ord(key[i].upper())) % 26)
        else:
            plaintxt += ciphertxt[i]
    return plaintxt