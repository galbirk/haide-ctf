#!/usr/bin/env python3
import threading
import socket
import subprocess

def handle_connection(s, addr):
  subprocess.call(r"C:\Windows\System32\cmd.exe", )# ("./home/root/bashjail.sh")

  s.sendall(
      ("Your input: >>>\n").encode())

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

