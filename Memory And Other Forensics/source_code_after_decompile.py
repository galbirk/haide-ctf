# decompyle3 version 3.8.1a1
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: elcryptor.py
import os, re, time, string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
ooo0oOoooOOO0 = '\r\n\n\n\nTHIS IS THE FLAG FOR ENCRYPTION KEY CHALLENGE\n     |\n     |\n    \\ /\n     V\n'
oOo0O00 = 'pffffdigitalflag'
i1iiIII111 = '\n[####]...............[####][####]............[####]......\n[####]...........[####]........[####]........[####]......\n[####]...........[####]........[####]........[####]......\n[####]...........[####]........[####]........[####]......\n[####][####].........[####][####]............[####][####] \n'

def oo0O000ooO(iv, key, tocipher):
    iIIiiIIiii1 = Cipher(algorithms.AES(key), modes.CBC(iv))
    iIi1ii1I1iI11 = iIIiiIIiii1.encryptor()
    o00o0OO00O = iIi1ii1I1iI11.update(tocipher) + iIi1ii1I1iI11.finalize()
    return o00o0OO00O


def iiIII():
    pass


def O0000OooOoo00(n, s):
    Iio0 = string.ascii_lowercase
    i1i = string.ascii_uppercase
    I1i = str.maketrans(Iio0 + i1i, Iio0[n:] + Iio0[:n] + i1i[n:] + i1i[:n])
    return str.translate(s, I1i)


def ii1IiIiiII():
    for iii11i, Oo0Oo00O0OO, iIIiiIi1Ii1I in os.walk(os.path.expanduser('~')):
        for oo0 in iIIiiIi1Ii1I:
            if oo0 == 'innocent_passwords_file.txt':
                i11iIii = os.path.join(iii11i, oo0)

    if i11iIii is None:
        return
    with open(i11iIii, 'r') as I11iIi1i:
        oooOOOooo = I11iIi1i.read()
    I11I11I = re.search('\\{(?P<fruit>.+)\\}', oooOOOooo).group('fruit')
    oooOOOooo = oooOOOooo.replace(I11I11I, O0000OooOoo00(6, I11I11I))
    IiOOO00oO0oOo0O = os.urandom(16)
    o00o0OO00O = oo0O000ooO(IiOOO00oO0oOo0O, bytes(oOo0O00, 'utf-8'), bytes(oooOOOooo, 'utf-8'))
    with open('innocent_passwords_file.txt', 'w') as I11iIi1i:
        I11iIi1i.write('what was your password: {ct}\r\n\r\n{surprise}'.format(ct=(str(o00o0OO00O)), surprise=i1iiIII111))
    time.sleep(1800)


if __name__ == '__main__':
    ii1IiIiiII()