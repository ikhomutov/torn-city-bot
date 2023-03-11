import multiprocessing
from multiprocessing import Process, Queue, Pipe
import socket
import random

HOST = "127.0.0.1"
PORT = 65432


def client(questions_queue, pipe_mapping):
    while True:
        pid, question = questions_queue.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(question.encode())
            data = s.recv(1024)
        result = data.decode('utf-8')
        pipe = pipe_mapping.get(pid)
        pipe.send(result)


def calc(question_queue, pipe):
    pid = multiprocessing.current_process().pid
    for _ in range(5):
        exp_1 = random.randint(1, 10)
        exp_2 = random.randint(1, 10)
        target_answer = exp_1 + exp_2
        question = f"{exp_1} + {exp_2} = ?"
        question_queue.put((pid, question))
        result = int(pipe.recv())
        print(f'Received answer: {result}')

        if result != target_answer:
            raise Exception(f'Wrong calculation. Expected: {target_answer}, received: {result}')


def main():
    question_queue = Queue()
    pipe_mapping = {}
    for _ in range(3):
        sender_conn, receiver_conn = Pipe()
        calc_process = Process(target=calc, args=(question_queue, receiver_conn))
        calc_process.start()
        pipe_mapping[calc_process.pid] = sender_conn

    client_process = Process(target=client, args=(question_queue, pipe_mapping))
    client_process.start()


if __name__ == '__main__':
    main()
