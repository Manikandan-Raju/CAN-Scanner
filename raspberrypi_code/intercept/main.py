import os
from can_receive import CanReceive
from can_send import CanSend


if __name__ == '__main__':
    os.system('sudo sh can-start.sh')
    can_receive_obj = CanReceive()
    can_send_obj = CanSend()
