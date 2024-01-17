# DF Key Exchange
from Crypto.PublicKey.DSA import generate
from random import SystemRandom
random = SystemRandom()

def generate_dh_parameters(bits=1024):
    DF = generate(bits)
    return DF.g, DF.p

class df_key:
    def __init__(self,g,p):
        self.g = g
        self.p = p

    def gen_privkey(self):
        # This number is kept private
        self.priv_key = random.randrange(start = 1,stop = self.p)

    def gen_pubkey(self):
        self.pub_key = pow(self.g,self.priv_key,self.p)

    def share_key(self,other_pub):
        self.share_key = pow(other_pub,self.priv_key,self.p)