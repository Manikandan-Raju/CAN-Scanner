import can


class CanReceive:
    def _init__(self):
        self.count = 0
        # noinspection PyTypeChecker
        self.bus_receive = can.interface.Bus(bustype='socketcan_native', channel='can1')

    def receive_data(self):
        receive_msg = self.bus_receive.recv()
        engine_speed_can = receive_msg.data[0]
        return engine_speed_can
