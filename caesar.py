# Caesar cipher
import string
plain_charset = string.ascii_uppercase

def encode(msg,key):
    ciphertext = ''
    for i in msg:
        if i in plain_charset:
            ciphertext += plain_charset[(plain_charset.find(i) + key) % len(plain_charset)]
        else:
            ciphertext += i
    return ciphertext

def decode(msg,key):
    plaintext = ''
    for i in msg:
        if i in plain_charset:
            plaintext += plain_charset[(plain_charset.find(i) - key) % len(plain_charset)]
        else:
            plaintext += i
    return plaintext

msg = input("Please enter your message in uppercase letters: ")
key = int(input("Please enter your shift value: ")) 
cipher = encode(msg,key)

print("Message:    ", msg)
print("Shift (key):", key)
print("Ciphertext: ", cipher)
