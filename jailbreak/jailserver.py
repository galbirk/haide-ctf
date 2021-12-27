#!/usr/bin/env python3
import threading
import socket
import subprocess

def handle_connection(s, addr):
  s.send("\r\nHello.\r\nwelcome to jailbreak challenge.".encode("utf-8"))
  while True:
      s.send("\r\n\nEnter your command >>> ".encode("utf-8"))
      d = s.recv(1024)
      if not d:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return
      idx = d.find(b'\n')
      line = d[:idx]
      command = [
        "/server/jail.sh", 
        line.decode("utf-8")
                ]
      try:
        response = subprocess.check_output(command)
      except:
        response = "invalid syntax".encode('utf-8')
      s.send(response)

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 7007))
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
