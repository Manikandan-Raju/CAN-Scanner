import can
import os
import time

os.system('sudo sh can-start.sh')

bus1 = can.interface.Bus(bustype='socketcan_native', channel='can1')


try:
    while True:
        msg = bus1.recv()
        print(msg)
except KeyboardInterrupt:
    os.system('ifconfig can1 down')
