import bluetooth  # Importing the Bluetooth Socket library

host = ""
port = 1  # Pi uses port 1 for Bluetooth Communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# Creatng Socket Bluetooth RFCOMM communication
print('Bluetooth Socket Created')

try:
    server.bind((host, port))
    print("Bluetooth Binding Completed")
except:
    print("Bluetooth Binding Failed")

server.listen(1)  # One connection at a time
client, address = server.accept()  # Server accepts the clients request and assigns a mac address.
print("Connected To", address)
print("Client:", client)

try:
    while (True):
        client.send("0")
        break  # Sending the data.
        data = client.recv(1024)  # Receivng the data. 1024 is the buffer size.
        print(data)

except:
    client.close()  # Closing the client connection
    server.close()  # Closing the server connection
