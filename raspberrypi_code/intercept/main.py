import os
from can_receive import CanReceive
from can_send import CanSend
from bluetooth_interface import BluetoothInterface
import time


if __name__ == '__main__':
    os.system('sudo sh can-start.sh')
    can_send_obj = CanSend()
    bluetooth_interface_obj = BluetoothInterface()
    while True:
        can_send_obj.edit_data()
        bluetooth_interface_obj.bluetooth_send()
