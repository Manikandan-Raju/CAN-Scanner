
import os
import can
import time





count =0
bus0 = can.interface.Bus(bustype='socketcan_native', channel='can0')
msg = can.Message(arbitration_id=0x700,data=[count,0x01,0x02, 0x03, 0x04, 0x05,0x06, 0x12],extended_id=True)
        



try:
    task = bus0.send_periodic(msg,1,duration=5)
    while True:
        #msg = can.Message(arbitration_id=0x700,data=[count,0x01,0x02, 0x03, 0x04, 0x05,0x06, 0x12],extended_id=True)
        msg.data[0] = count
        task.modify_data(msg)
        count += 1
        if count <= 5:
                print("{}: {}".format(msg.arbitration_id, msg.data))
        time.sleep(0.5)
        


except KeyboardInterrupt:
    os.system('ifconfig can0 down')
