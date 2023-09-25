import time

from .ctrl_table import CtrlTable
from .constants import MIN_ANGLE, MAX_ANGLE


class Servo:
    """Represents a servomotor"""

    def __init__(self, servo_id, interface):
        self.servo_id = servo_id
        self.interface = interface

        self.set_angle_limits()
        self._set_shutdown_error()

    def _set_shutdown_error(self):
        """Enable shutdown error if goal_position is outside of range"""
        val = self.interface.read(self.servo_id, CtrlTable.Shutdown)
        self.interface.write(self.servo_id, CtrlTable.Shutdown, val | 0b10)

    def blink(self, duration=5):
        """Make the motor's LED blink"""
        for _ in range(duration):
            self.interface.write(self.servo_id, CtrlTable.LED, 1)
            time.sleep(0.5)
            self.interface.write(self.servo_id, CtrlTable.LED, 0)
            time.sleep(0.5)

    def set_enable_torque(self, enable_torque):
        """Activate/Desactivate torque"""
        self.interface.write(
            self.servo_id, CtrlTable.TorqueEnable, 1 if enable_torque else 0
        )

    def set_goal_position(self, value):
        """Change goal position for the motor"""
        value = max(min(value, MAX_ANGLE), MIN_ANGLE)

        self.interface.write(self.servo_id, CtrlTable.GoalPosition, value)

    def set_angle_limits(self, min_value=MIN_ANGLE, max_value=MAX_ANGLE):
        """Set angle limit for the motor

        Warning, only using this will not prevent motor to go out range,
        need to activate shutdown error.
        """
        self.interface.write(self.servo_id, CtrlTable.CWAngleLimit, min_value)
        self.interface.write(self.servo_id, CtrlTable.CCWAngleLimit, max_value)

    def get_position(self):
        """Returns motor current position"""
        return self.interface.read(self.servo_id, CtrlTable.PresentPosition)

    def get_model_number(self):
        """Returns motor model number"""
        return self.interface.read(self.servo_id, CtrlTable.ModelNumber)
