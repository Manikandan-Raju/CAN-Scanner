import bluetooth  # Importing the Bluetooth Socket library
import time
from can_receive import CanReceive

can_receive_obj = CanReceive()


class BluetoothInterface:

    def __init__(self):
        self.start = 0
        self.count = 1
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
        try:
            print("Waiting for bluetooth connection")
            self.client, self.address = self.server.accept()

        except:
            print("Waiting for bluetooth connection")
            time.sleep(30)
            print("Bluetooth is not connected")
        finally:
            print("Connected To", self.address)
            print("Client:", self.client)

    def bluetooth_send(self):
        if self.count > 5:
            self.count = 1
        self.client.send(str(self.count) + str(can_receive_obj.receive_data()))  # Sending the data.

        self.count += 1

    def bluetooth_close(self):
        self.client.close()  # Closing the client connection
        self.server.close()  # Closing the server connection
