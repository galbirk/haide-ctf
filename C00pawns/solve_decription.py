import os 
import re
import string
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

# FIND IN MEM IMAGE, in address space of python6.py script
KEY         = 'pffffdigitalflag'   
# FIND IN MEM IMAGE, in strings of notepad.exe
TO_UNCIPHER = b'~\x07,\xc4\xd7\xd0\xf6\n\xc2\xd8\xb7q\x8ap\xf8\xef\xb0g\x1e\xcb\xf1\xdfK\xb0\x1e\xe8\x193\xe6J\xd7\xa5'


def aes_decrypt(iv, key, touncipher):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dt = decryptor.update(touncipher) + decryptor.finalize()
    return (dt)

# CAN SOLVE WITH
# 1. CYBERCHEFF ROT.
# 2. BRUTE FORCE, USING FUNC FROM PYTHON6.py FILE,
 
def rot_n(n, s):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return str.translate(s, trans)

def rot_decipher(Cfruit):
    for i in range(len(string.ascii_lowercase)):
        print('rot_{i}: {dt}'.format(i=i, dt=rot_n(i, Cfruit) ))


def main():
    iv = os.urandom(16)
    dt = aes_decrypt(iv, bytes(KEY, 'utf-8'), TO_UNCIPHER)
    print('''                       
ciphered:   {ct} 
len(ct):    {len_ct}
unciphered: {dt}
'''.format(ct=TO_UNCIPHER, len_ct=len(TO_UNCIPHER), dt=dt))   # gives: b'000000000000000000000FLAG{Magbg}'

    fruit = rot_decipher('Magbg')  # ans is rot 6. (opposite of 20)
    
    #finally, flag is:
    print ('FLAG{Guava}')

if __name__ == "__main__":
    main()