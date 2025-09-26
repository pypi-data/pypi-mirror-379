from .client_view import start_client

class Server:
    @staticmethod
    def start(server_ip=None, port=5000, password="hyper11os"):
        """Start the client (connect to server)."""
        start_client(server_ip=server_ip, port=port, password=password)

server = Server()
