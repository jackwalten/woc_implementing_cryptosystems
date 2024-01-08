# RSA Cryptosystem
from random import SystemRandom
random = SystemRandom()

# Sieving for small primes
first_primes_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881]

def nbitodd(bits):
    p = random.getrandbits(bits)
    if p % 2 == 0:
        return p + 1
    else:
        return p

def miller_rabin(p):
    # p - 1 = (2^k)*m
    m = p - 1
    k = 0
    while m % 2 == 0:
        k += 1
        m = m // 2
    steps = 64 # FIPS 186-4
    for i in range(steps):
        a = random.randint(2,p-2)
        x = pow(a,m,p)
        for j in range(k):
            y = pow(x,2,p)
            if y == 1 and x != 1 and x != p - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

def check_primality(p):
    # First low level check of small primes
    for num in first_primes_list:
        if p % num == 0:
            return False
    else:
        # Do miller rabin
        return miller_rabin(p)

def generate_prime(bits=1024):
    # This is almost identical to openssl's implementation
    # https://github.com/openssl/openssl/blob/master/crypto/bn/bn_prime.c
    p = nbitodd(bits)
    while True:
        if check_primality(p):
            break
        p += 2
    return p