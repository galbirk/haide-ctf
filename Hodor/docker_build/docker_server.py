#!/usr/bin/env python3
import threading
import socket
import math


with open("flag.txt", "r") as f:
  FLAG = f.read().strip()

def pad (v):
    f2 = FLAG
    while (len(v) < len(f2)):    #f2 is longer, pad v to match
        f2 = f2[:len(v)]
    while (len(f2) < len(v)):    #v is longer, pad f2 to match
        f2 += v[len(f2)%len(v)]
    return v, f2

def pow (v):
  return int(math.pow(len(FLAG), len(v)))

def mod (v):
    v, f = pad (v)
    ans = []
    for idx in range(min(len(v), len(f))):
        ans.append(str((ord(v[idx]) + ord(f[idx])) % 2))
    return '-'.join(ans)

def div (v):
    v, f = pad (v)
    ans = []
    for idx in range(min(len(v), len(f))):
        ans.append(str(math.floor((ord(v[idx]) + ord(f[idx])) / 2))) 
    return '-'.join(ans)


ARITHMETIC_FUNCS = [
  pow,
  mod,
  div
]


def handle_connection(s, addr):
  s.sendall(
      ("Please enter your guess \n"
       "and I'll show you the calculation results!\n"
       "Note: the flag consists only of the characters: [a-z]\n").encode())

  data = b''
  while True:
    idx = data.find(b'\n')
    if idx == -1:
      if len(data) > 128:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return

      d = s.recv(1024)
      if not d:
        s.close()
        return
      data += d
      continue

    line = data[:idx]
    data = data[idx+1:]

    test_string = line.decode("utf-8") 

    response = []
    response.append('')
    for afunc in ARITHMETIC_FUNCS:
      res = afunc(test_string)
      response.append(f"{afunc.__name__:>8} {res:>4}")
    response.append('')
    response.append('')
    s.sendall('\n'.join(response).encode())
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

