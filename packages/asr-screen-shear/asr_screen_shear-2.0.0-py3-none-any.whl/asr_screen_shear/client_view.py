import socket, struct, io
import numpy as np
import cv2

def start_client(server_ip=None, port=5000, password="hyper11os"):
    if server_ip is None:
        server_ip = input("Enter server IP: ")
        
    def recv_exact(sock, n):
        buf = b""
        while len(buf) < n:
            chunk = sock.recv(n - len(buf))
            if not chunk:
                raise RuntimeError("socket closed")
            buf += chunk
        return buf

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        pw_bytes = password.encode("utf-8")
        s.sendall(struct.pack("!H", len(pw_bytes)))
        s.sendall(pw_bytes)
        resp = s.recv(2)
        if resp != b"OK":
            print("[CLIENT] Server rejected password or no response. Exiting.")
            return
        print("[CLIENT] Connected and authenticated. Receiving frames...")

        try:
            while True:
                size_data = recv_exact(s, 8)
                size = struct.unpack("!Q", size_data)[0]
                img_bytes = recv_exact(s, size)
                nparr = np.frombuffer(img_bytes, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                if img is None:
                    continue
                cv2.imshow("Remote Screen", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print("[CLIENT] Connection closed or error:", e)
        finally:
            cv2.destroyAllWindows()
