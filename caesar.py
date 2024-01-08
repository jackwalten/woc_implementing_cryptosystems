# Caesar cipher
def encrypt(plaintxt,key=13):
    ciphertxt = ''
    for char in plaintxt:
        if char.islower():
            ciphertxt += chr(ord('a') + (ord(char) - ord('a') + key) % 26)
        elif char.isupper():
            ciphertxt += chr(ord('A') + (ord(char) - ord('A') + key) % 26)
        else:
            ciphertxt += char
    return ciphertxt 

def decrypt(ciphertxt,key=13):
    return encrypt(ciphertxt,26-key)