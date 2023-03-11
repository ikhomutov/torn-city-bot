import socket

HOST = "127.0.0.1"
PORT = 65432


def client(to_send):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(to_send.encode())
        data = s.recv(1024)
    return data.decode('utf-8')


if __name__ == '__main__':
    to_calc = [
        (1, 2, 3),
        (2, 2, 4),
        (4, 6, 10)
    ]
    for exp in to_calc:
        to_send = f"{exp[0]} + {exp[1]} = ?"
        received = client(to_send)
        answer = int(received)
        print(f'Received answer: {answer}')

        if answer != exp[2]:
            raise Exception('Wrong calculation')
