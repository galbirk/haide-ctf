#!/usr/bin/env python3
import threading
import socket
import subprocess

def handle_connection(s, addr):

  while True:
      s.send("Enter your command: ".encode("utf-8"))
      d = s.recv(1024)
      if not d:
        s.close()
        return
      idx = d.find(b'\n')
      line = d[:idx]
      response=subprocess.check_output(["/root/test.sh",line.decode("utf-8")])
      s.send(response)
      continue
    
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

