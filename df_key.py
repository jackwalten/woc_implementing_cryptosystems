# DF Key Exchange
# Since python is a horrendously slow language, I give up and use the rust based cryptography library. Thank you python!!!
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from random import SystemRandom
random = SystemRandom()

def generate_dh_paramters(bits=512):
    parameters = dh.generate_parameters(generator=2,key_size=bits,backend=default_backend())
    return parameters.parameter_numbers().g,parameters.parameter_numbers().p

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