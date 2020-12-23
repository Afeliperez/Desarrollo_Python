import socket #librería para conectar a la red

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #protocolo de comunicacion
mysock.connect(('data.pr4e.org', 80)) # se conecta con el host y el puerto (80)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #método requerido es Get y se ingresa la url del sitio  y termina con el protocolo
mysock.send(cmd) # se envía un comando

while True:
    data = mysock.recv(512) # la variable data recibe 512 caracteres
    if len(data) < 1:
        break
    print(data.decode(),end='') #decodifica

mysock.close() #cierra la conección con el socket