import socket

HOST = "127.0.0.1"
PORT = 65432


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode('utf-8')}")
                    answer = input()
                    conn.sendall(answer.encode('utf-8'))


if __name__ == '__main__':
    server()