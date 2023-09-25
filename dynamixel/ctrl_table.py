from enum import Enum


class CtrlTable(Enum):
    # Control Table of EEPROM Area
    ModelNumber = 0
    FirmWareVersion = 2
    ID = 3
    BaudRate = 4
    ReturnDelayTime = 5
    CWAngleLimit = 6
    CCWAngleLimit = 8
    TemperatureLimit = 11
    MinVoltageLimit = 12
    MaxVoltageLimit = 13
    MaxTorque = 14
    StatusReturnLevel = 16
    AlarmLED = 17
    Shutdown = 18

    # Control Table of RAM Area
    TorqueEnable = 24
    LED = 25
    CWComplianceMargin = 26
    CCWComplianceMargin = 27
    CWComplianceSlope = 28
    CCWComplianceSlope = 29
    GoalPosition = 30
    MovingSpeed = 32
    TorqueLimit = 34
    PresentPosition = 36
    PresentSpeed = 38
    PresentLoad = 40
    PresentVoltage = 42
    PresentTemperature = 43
    Registered = 44
    Moving = 46
    Lock = 47
    Punch = 48

    """size in bytes to write/read
    """

    def size(self):
        size_1_byte = [
            2,
            3,
            4,
            5,
            11,
            12,
            13,
            16,
            17,
            18,
            24,
            25,
            26,
            27,
            28,
            29,
            42,
            43,
            44,
            46,
            47,
        ]

        if self.value in size_1_byte:
            return 1
        else:
            return 2

