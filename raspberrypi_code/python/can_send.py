
import os
import can
import time

bus0 = can.interface.Bus(bustype='socketcan_native', channel='can0')

try:
    while True:
        msg = can.Message(arbitration_id=0x7de,data=[count,0x01,0x02, 0x03, 0x04, 0x05,0x06, 0x12],extended_id=True)
        bus0.send(msg)
        print("{}: {}".format(msg.arbitration_id, msg.data))
        time.sleep(1)



except KeyboardInterrupt:
    os.system('ifconfig can0 down')
