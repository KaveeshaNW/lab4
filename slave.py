import socket
host = ’192.168.1.10’ # Replace with Master Pi’s IP
port = 5000
client = socket.socket()
client.connect((host, port))
client.send("Hello from slave".encode())
data = client.recv(1024).decode()
print("Received from server:", data)

client.close()