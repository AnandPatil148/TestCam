import cv2
import socket
import pickle
import struct

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '180.ip.ply.gg'  # Replace with the IP address of the streaming server
port = 12378
socket_address = (host_ip, port)

# Connect to the server
client_socket.connect(socket_address)

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Serialize the frame
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))  # Pack the message size as a 4-byte long integer
    
    # Send the message size followed by the serialized frame to the client
    client_socket.sendall(message_size + data)
    

    # Display the streamed frame
    #cv2.imshow('Streaming Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
client_socket.close()
