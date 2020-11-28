import can
import time


class CanSend:

    def __init__(self):
        self.count = 0
        self.msg = can.Message(arbitration_id=0x700, data=[0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x12],
                               extended_id=True)

        self.bus = can.interface.Bus(bustype='socketcan_native', channel='can0')
        self.bus_send_task = self.bus.send_periodic(self.msg, 1)
        self.data = 0

    def edit_data(self):
        self.count += 1
        self.msg.data[0] = self.count
        self.bus_send_task.modify_data(self.msg)
        if self.count >= 99:
            self.count = 0
        print("{}: {}".format(self.msg.arbitration_id, self.msg.data))
        time.sleep(0.5)
