import socket

class Disconnect:
    @staticmethod
    def qemuserver(server_ip, port=5000):
        """Disconnect client from server by closing the connection."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((server_ip, port))
                s.shutdown(socket.SHUT_RDWR)
            print("[DISCONNECT] Server disconnected from client.")
        except Exception as e:
            print("[DISCONNECT] Error:", e)

qemuserver = Disconnect()
