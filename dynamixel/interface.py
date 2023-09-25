from dynamixel_sdk import PortHandler, PacketHandler, COMM_SUCCESS

from .servo import Servo
from .ctrl_table import CtrlTable
from .constants import BAUDRATE, PORT
from .exceptions import TxRxError, RxPacketError

class Interface:
    """Help have a representation of connected servomotors"""

    def __init__(self, device_name=PORT, protocol_ver=1.0):
        self._motors = {}

        self.port_handler = PortHandler(device_name)
        self.packet_handler = PacketHandler(protocol_ver)

        # Open port
        if self.port_handler.openPort():
            print(f"Successed to open the port {0}", device_name)
        else:
            raise RuntimeError("Failed to open port")

        self._set_bauderate(BAUDRATE)

        self.discover()

    def _set_bauderate(self, baudrate):
        """Change bauderate of to port handler"""
        if self.port_handler.setBaudRate(baudrate):
            print("Succeeded to change the baudrate")
        else:
            self.port_handler.closePort()
            raise RuntimeError("Failed to change the baudrate")

    def write(self, servo_id: int, addr: CtrlTable, value: int):
        """Call the write function adapted to the asked data"""
        if not type(addr) == CtrlTable:
            raise RuntimeError("Wrong parameter for write call")

        if addr.size() == 1:
            result, error = self.packet_handler.write1ByteTxRx(
                self.port_handler, servo_id, addr.value, value
            )
        elif addr.size() == 2:
            result, error = self.packet_handler.write2ByteTxRx(
                self.port_handler, servo_id, addr.value, value
            )
        else:
            raise RuntimeError("TODO, unsuported byte size for write")

        if result != COMM_SUCCESS:
            err = format("%s" % self.packet_handler.getTxRxResult(result))
            raise TxRxError(err)
        elif error != 0:
            err = format("%s" % self.packet_handler.getRxPacketError(error))
            raise RxPacketError(err)

    def read(self, servo_id: int, addr: CtrlTable):
        """Call the read function adapted to the asked data"""
        value = None

        if not type(addr) == CtrlTable:
            raise RuntimeError("Wrong parameter for read call")

        if addr.size() == 1:
            value, result, error = self.packet_handler.read1ByteTxRx(
                self.port_handler, servo_id, addr.value
            )
        elif addr.size() == 2:
            value, result, error = self.packet_handler.read2ByteTxRx(
                self.port_handler, servo_id, addr.value
            )
        else:
            raise RuntimeError("TODO, unsuported byte size for read")

        if result != COMM_SUCCESS:
            err = format("%s" % self.packet_handler.getTxRxResult(result))
            raise TxRxError(err)
        elif error != 0:
            err = format("%s" % self.packet_handler.getRxPacketError(error))
            raise RxPacketError(err)

        return value

    def discover(self, id_range=(1, 18)):
        """Try to reach each id in id_range and fill self._motors"""
        for id in range(id_range[0], id_range[1] + 1):
            try:
                if self.read(id, CtrlTable.ID) == id:
                    self._motors[id] = Servo(id, self)
            except TxRxError:
                continue

    def update_motors(self, instr):
        """For each motors of the instr dictionary, apply the goal position

        This function is fallproof in case of a missing motor.

        instr: Dict{motor_id: goal_position}
        """

        for id, goal in instr.items():
            if id not in self._motors:
                continue

            try:
                self._motors[id].set_goal_position(goal)
            except (TxRxError, RxPacketError) as err:
                print(f"Failed to update motor {id}: {err}")
                continue

    def get_servo(self, servo_id):
        """If found, retunrs the Servo object corresponding to passed id"""
        if servo_id not in self._motors:
            return None

        return self._motors[servo_id]

    def close(self):
        """Close communication"""
        self.port_handler.closePort()
