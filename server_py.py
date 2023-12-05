import socket


server = socket.socket()
file_to_stream = 'test_file.exe'
server.bind(('127.0.0.1', 9000))
server.listen()

the_file = open(file_to_stream, 'rb')
content = the_file.read()
metadata_set: dict[str, str | int] = {
    'filename': the_file.name,
    'filelen':  len(content)
}
metadata =  "\r\r".join([str(metadata_set[x]) for x in metadata_set.keys()]).encode()
print("Server is listening 127.0.0.1:9000...")
the_file.close()
while True:
    client_socket, _ = server.accept()
    client_socket.send(str(len(metadata)).encode())
    client_socket.send(metadata)
    client_socket.send(content)
    client_socket.close()
