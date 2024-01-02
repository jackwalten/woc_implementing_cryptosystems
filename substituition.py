# Substitution cipher
plain_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_charset = 'ZEBRASCDFGHIJKLMNOPQTUVWXY'

def encode(msg):
    ciphertext = ''
    for i in msg:
        if i in plain_charset:
            ciphertext += cipher_charset[plain_charset.find(i)]
        else:
            ciphertext += i
    return ciphertext

def decode(msg):
    plaintext = ''
    for i in msg:
        if i in cipher_charset:
            plaintext += plain_charset[cipher_charset.find(i)]
        else:
            plaintext += i
    return plaintext

msg = input("Please enter your message in uppercase letters: ")
enc = encode(msg)
dec = decode(enc)
print("Plaintext Alphabet: ", plain_charset)
print("Ciphertext Alphabet:", cipher_charset)
print("Message:", msg)
print("Encoded:", enc)
print("Decoded:", dec)
