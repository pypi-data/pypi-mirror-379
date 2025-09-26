import socket, io, struct, time
import pyautogui
from PIL import Image
import netifaces

def get_local_ip():
    try:
        for iface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                for addr in addrs[netifaces.AF_INET]:
                    ip = addr['addr']
                    if ip != "127.0.0.1":
                        return ip
    except Exception:
        pass
    return "0.0.0.0"

def send_all(sock, data):
    totalsent = 0
    while totalsent < len(data):
        sent = sock.send(data[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent += sent

def start_server(port=5000, password="hyper11os"):
    HOST = get_local_ip()
    print(f"[SERVER] Detected local IP: {HOST}")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port))
        s.listen(1)
        print(f"[SERVER] Listening on {HOST}:{port} — waiting for client...")
        
        conn, addr = s.accept()
        with conn:
            print("[SERVER] Client connected:", addr)
            pw_len_data = conn.recv(2)
            if not pw_len_data:
                print("[SERVER] No handshake received. Closing.")
                return
            pw_len = struct.unpack("!H", pw_len_data)[0]
            pw = conn.recv(pw_len).decode("utf-8")
            
            if pw != password:
                print("[SERVER] Bad password — closing.")
                conn.sendall(b"NO")
                return
            conn.sendall(b"OK")
            print("[SERVER] Handshake ok — streaming started.")

            try:
                while True:
                    im = pyautogui.screenshot()
                    buf = io.BytesIO()
                    im.save(buf, format="JPEG", quality=60)
                    data = buf.getvalue()
                    send_all(conn, struct.pack("!Q", len(data)))
                    send_all(conn, data)
                    time.sleep(0.08)
            except (BrokenPipeError, ConnectionResetError):
                print("[SERVER] Client disconnected.")
