# HAHA

import os 
import re
import time
import string
import random
import webbrowser
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

HINT = '''\r\n\n\n
THIS IS THE FLAG FOR ENCRYPTION KEY CHALLENGE
     |
     |
    \ /
     V
'''
KEY  = 'pffffdigitalflag'   # <-- THIS IS THE FLAG FOR THE CHALLENGE
BANNER = '''
[####]...............[####][####]............[####]......
[####]...........[####]........[####]........[####]......
[####]...........[####]........[####]........[####]......
[####]...........[####]........[####]........[####]......
[####][####].........[####][####]............[####][####] 
'''
url = r'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpikbest.com%2Fso%2Ffruit-coupons.html&psig=AOvVaw3lc_BQWoiwut_Y4aioaASq&ust=1640705990852000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMDgjKuohPUCFQAAAAAdAAAAABAJ'


def encrypt(iv, key, tocipher):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(tocipher) + encryptor.finalize()
    return (ct)

# haha, you thought i'de give you that !? (:
def decrypt():
    pass

def rot_n(n, s):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return str.translate(s, trans)



def main():

    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            if ("innocent_passwords_file" in file):
                if ("corrupt" in file):
                    print(os.path.join(root, file))
                    time.sleep(30*60) # hour sleep - stay running for memory dump
                else:
                    target = (os.path.join(root, file))
                    
    if (target is None):
        return

    with open (target, 'r') as f:
        passwords = f.read()
    
    fruit = re.search('\{(?P<fruit>.+)\}', passwords).group('fruit')
    passwords = passwords.replace(fruit, rot_n(random. randint(2,25), fruit))

    iv = os.urandom(16)
    ct = encrypt(iv, bytes(KEY, 'utf-8'), bytes(passwords, 'utf-8'))
    
    with open (target, 'w') as f:
        f.write('what was your password: {ct}\r\n\r\n{surprise}'.format(ct=str(ct), surprise=BANNER))

    os.rename(target,"{filename}.corrupt.txt".format(filename=target))


if __name__ == "__main__":
    webbrowser.open(url)
    main()
