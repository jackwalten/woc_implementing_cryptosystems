# Atbash cipher
def encrypt(plaintxt):
    ciphertxt = ''
    for char in plaintxt:
        if char.islower():
            ciphertxt += chr(25 - ord(char) + 2*ord('a'))
        elif char.isupper():
            ciphertxt += chr(25 - ord(char) + 2*ord('A'))
        else:
            ciphertxt += char
    return ciphertxt

def decrypt(ciphertxt):
    return encrypt(ciphertxt)