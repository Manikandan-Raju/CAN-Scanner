import can
import time


class CanSend:
    def _init__(self):
        self.count = 0
        self.bus_send = can.interface.Bus(bustype='socketcan_native', channel='can0')
        self.msg = can.Message(arbitration_id=0x700, data=[self.count, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x12], extended_id=True)
        self.send_task = self.bus_send.send_periodic(self.msg, 1, duration=5)

    def edit_data(self):
        self.msg.data[0] = self.count
        self.send_task.modify_data(self.msg)
        self.count += 1
        if self.count <= 5:
            print("{}: {}".format(self.msg.arbitration_id, self.msg.data))
        time.sleep(0.5)
