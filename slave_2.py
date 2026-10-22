import socket
host = '172.20.133.68' # Replace with Master Pi’s IP
port = 5000
client = socket.socket()
client.connect((host, port))
while True:
    x=input("enter msg:")
    if x=="exit":
        break
    client.send(x.encode())
    data = client.recv(1024).decode()
    print("Received from server:", data)
client.close()
