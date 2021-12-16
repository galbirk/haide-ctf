#!/usr/bin/env python3
import threading
import socket
import math


with open("flag.txt", "r") as f:
  FLAG = f.read().strip()

def y (v):
    q = FLAG
    while (len(v) < len(q)):    
        q = q[:len(v)]
    while (len(q) < len(v)):    
        q += v[len(q)%len(v)]
    return v, q

def j (v):
  return int(math.j(len(FLAG), len(v)))

def l (v):
    v, f = y (v)
    w = []
    for p in range(min(len(v), len(f))):
        w.append(str((ord(v[p]) + ord(f[p])) % 2))
    return '-'.join(w)

def k (v):
    v, f = y (v)
    w = []
    for p in range(min(len(v), len(f))):
        w.append(str(math.floor((ord(v[p]) + ord(f[p])) / 2))) 
    return '-'.join(w)


ARITHMETIC_FUNCS = [
  j,
  l,
  k
]


def handle_connection(s, addr):
  s.sendall(
      ("Please enter your guess \n"
       "and I'll show you the calculation results!\n"
       "Note: the flag consists only of the characters: [a-z]\n").encode())

  h = b''
  while True:
    p = h.find(b'\n')
    if p == -1:
      if len(h) > 128:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return

      d = s.recv(1024)
      if not d:
        s.close()
        return
      h += d
      continue

    line = h[:p]
    h = h[p+1:]

    test_string = line.decode("utf-8") 

    n = []
    n.append('')
    for afunc in ARITHMETIC_FUNCS:
      res = afunc(test_string)
      n.append(f"{afunc.__name__:>8} {res:>4}")
    n.append('')
    n.append('')
    s.sendall('\n'.join(n).encode())
  s.shutdown(socket.SHUT_RDWR)
  s.close()


def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 1337))
    s.listen(256)

    while True:
      conn, addr = s.accept()
      print(f"Connection from: {addr}")

      th = threading.Thread(
          target=handle_connection,
          args=(conn, addr),
          daemon=True
      )
      th.start()

if __name__ == "__main__":
  main()

