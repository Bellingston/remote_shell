#import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('127.0.0.1',8888))
#s.listen(3)
#while True:
#    try:
#        client, addr = s.accept()
#        while True:
#            result = client.recv(1024).decode('utf-8')
#            if not result:
#                break
#            print(addr, ': ', result)        
#        client.close()
#    except KeyboardInterrupt:
#        s.close()
#        break
#    else:
#        result = client.recv(1024)
#        print(f"{addr}: {result.decode('utf-8')}")



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9119))
s.listen(5)
client, addr = s.accept()
while True:
    command = str(input('Enter command: '))
    client.send(command.encode('utf-8'))
    if command == 'exit':
        break
    result_output = client.recv(4096).decode('utf-8')
    print(result_output)
client.close()
s.close()










