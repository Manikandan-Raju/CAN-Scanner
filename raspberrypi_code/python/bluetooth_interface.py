import bluetooth  # Importing the Bluetooth Socket library


class BluetoothInterface:

    def __init__(self):
        self.host = ""
        self.port = 1  # Pi uses port 1 for Bluetooth Communication
        self.server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  # Creating Socket Bluetooth RFCOMM communication
        print('Bluetooth Socket Created')
        try:
            self.server.bind((self.host, self.port))
            print("Bluetooth Binding Completed")
        except:
            print("Bluetooth Binding Failed")
        self.server.listen(1)  # One connection at a time
        self.client, self.address = self.server.accept()  # Server accepts the clients request and assigns a mac address.
        print("Connected To", self.address)
        print("Client:", self.client)

    def bluetooth_send(self):
        self.client.send("0")  # Sending the data.

    def bluetooth_close(self):
        self.client.close()  # Closing the client connection
        self.server.close()  # Closing the server connection
