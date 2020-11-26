import can


class CanReceive:
    def _init__(self):
        self.count = 0
        self.bus_receive = can.interface.Bus(bustype='socketcan_native', channel='can1')
        self.receive_msg = self.bus_receive.recv()

    def receive_data(self):
        engine_speed_can = self.receive_msg.data[0]
        return engine_speed_can
