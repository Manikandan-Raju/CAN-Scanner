import can
import time
from database import Data
data = Data()


class CanSend:

    def _init__(self):
        self.count = 0
        self.msg = can.Message(arbitration_id=0x700, data=[0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x12],
                               extended_id=True)
        # noinspection PyTypeChecker
        self.bus_send_task = can.interface.Bus(bustype='socketcan_native', channel='can0').send_periodic(self.msg,
                                                                                                         data.msg_interval,
                                                                                                         data.msg_duration)
        self.data = 0

    def edit_data(self):
        self.msg.data[0] = self.count
        self.bus_send_task.modify_data(self.msg)
        self.count = self.count + 1
        if self.count >= 99:
            # noinspection PyAttributeOutsideInit
            self.count = 0
        print("{}: {}".format(self.msg.arbitration_id, self.msg.data))
        time.sleep(0.5)
