import socket

ip = input("Ingresa la IP: ")

for port in range(1, 65535):
    client = socket.socket()
    client.settimeout(0.05)
    if client.connect_ex((ip, port)) == 0:
        print(f"[>] Puerto [{port}] Abierto")
