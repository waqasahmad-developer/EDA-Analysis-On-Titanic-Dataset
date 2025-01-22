import time
import socket
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen()  # Start listening for connections

print("Server is listening on port 9999...")

while True:
    client, addr = server.accept()  # Accept a connection
    print("Connection from", addr)
    client.send("You Are Connected!\n".encode())  # Send a welcome message
    
    # Send part of the Iris dataset
    message = f"data: {data['data'][:, 0].tolist()}\n"  # Convert NumPy array to a list for serialization
    client.send(message.encode())
    
    time.sleep(1)  # Pause for 1 second before disconnecting
    client.send("You Are Being Disconnected!\n".encode())  # Notify the client about disconnection
    client.close()  # Close the client connection
