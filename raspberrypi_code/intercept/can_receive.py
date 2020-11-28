import can
import time

engine_speed_can = 0


class CanReceive:
    def __init__(self):
        self.count = 0
        self.bus = can.interface.Bus(bustype='socketcan_native', channel='can1')

    def receive_data(self):
        receive_msg = self.bus.recv()
        print(receive_msg)
        engine_speed_can = receive_msg.data[0]
        print(engine_speed_can)
        return engine_speed_can
