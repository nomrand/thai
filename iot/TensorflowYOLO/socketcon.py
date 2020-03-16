import time
import socket
import pickle
import cv2

BUFFER_SIZE = 1024
PORT = 50001


def server(callback):
    print("[SV]LOOP START")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # IPアドレスとポートを指定
        s.bind(('0.0.0.0', PORT))
        # 1 接続
        s.listen(1)
        # connection するまで待つ
        while True:
            # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
            conn, addr = s.accept()
            print('[SV]CL ADDR: {} {}'.format(addr, time.time()))
            with conn:
                # データを受け取る
                req_b = recv_all(conn)
                try:
                    req = pickle.loads(req_b)
                except pickle.UnpicklingError:
                    print("[SV]RECV PARTIAL DATA {}".format(time.time()))
                    conn.sendall(pickle.dumps(None))
                    continue

                print("[SV]REQ  RECV:{}({}) {}".format(
                    type(req), len(req_b), time.time()))

                resp = callback(req)
                resp_b = pickle.dumps(resp)
                print("[SV]RESP SEND:{}({}) {}".format(
                    type(resp), len(resp_b), time.time()))
                conn.sendall(resp_b)


def client(server, req):
    print("[CL]REQ SEND START {}".format(time.time()))
    req_b = pickle.dumps(req)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバを指定
        s.connect((server, PORT))

        s.sendall(req_b)
        print("[CL]REQ  SEND:{}({}) {}".format(
            type(req), len(req_b), time.time()))

        resp_b = recv_all(s)
        resp = pickle.loads(resp_b)
        print("[CL]RESP RECV:{}({}) {}".format(
            type(resp), len(resp_b), time.time()))
        return resp


def recv_all(sock):
    data_all = b''
    sock.settimeout(1)
    while True:
        try:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                if data_all:
                    return data_all
            data_all += data
            # if len(data) < BUFFER_SIZE:
            #     return data_all

        except socket.timeout:
            if data_all:
                return data_all


if __name__ == "__main__":
    import threading
    thread_s = threading.Thread(target=lambda: server(
        lambda x: "***[" + str(x.shape[0]) + ", " + str(x.shape[1]) + "]***"
    ))
    thread_s.start()

    time.sleep(1)

    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()

    thread_c = threading.Thread(target=lambda: print("CLIENT RESP:", client(
        "127.0.0.1",
        frame
    )))
    thread_c.start()
