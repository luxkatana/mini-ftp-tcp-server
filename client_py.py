import socket
import os


client = socket.socket()

destination_root = "./dest/"
client.connect(('127.0.0.1', 9000))


metadata_len = client.recv(50).decode()
if not metadata_len.isnumeric():
    print("First response is not an int (metadata-len expected)")
    exit(1)

metadata: str = client.recv(int(metadata_len)).decode()

filename, content_len = metadata.split('\r\r')

content = client.recv(int(content_len))
with open(os.path.join(destination_root, filename), 'wb') as file:
    file.write(content)

client.close()
