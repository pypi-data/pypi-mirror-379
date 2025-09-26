from .server_share import start_server

class PC2:
    @staticmethod
    def start(port=5000, password="hyper11os"):
        """Start the server."""
        start_server(port=port, password=password)

pc2 = PC2()
