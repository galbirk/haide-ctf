#!/usr/bin/env python3
import threading
import socket
import subprocess
import shlex

def handle_connection(s, addr):

    while True:
        s.send("\r\n\nEnter your command >>> ".encode("utf-8"))
        d = s.recv(1024)
        if not d:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return
        idx = d.find(b'\n')
        line = d[:idx]
        command = [ "./jail.sh" ]
        userInput = shlex.split(line.decode("utf-8"))
        print(userInput)
        print(type(userInput))
        print(len(userInput))
        if (len(userInput) < 7): command += userInput
        else: 
            s.send('command is too long.\r\n'.encode('utf-8'))
            continue
        """
        try:
            response = subprocess.check_output(command)
        except:
            response = "invalid syntax\r\n".encode('utf-8')
        """
        response = subprocess.check_output(command)
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
