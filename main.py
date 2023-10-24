#!/usr/bin/python

# https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/

import time
from dynamixel.interface import Interface
from dynamixel.constants import MID_ANGLE, MIN_ANGLE


def main():
    interface = Interface()

    # It will find all motors connected to the computer with id between 1 and 18
    interface.discover()

    for i in interface._motors:
        print(f"Motor #{i} found")

    time.sleep(1)

    # Get the motor with id 1, 2 and 3
    servo_01 = interface.get_servo(1)
    servo_02 = interface.get_servo(2)
    servo_03 = interface.get_servo(3)

    if servo_01 and servo_02 and servo_03:

        commands = {
            "hello": lambda: hello_command(interface),
            "walkf": lambda: walkf_command(interface),
            "walkb": lambda: walkb_command(interface)
        }

        while True:
            #Value for my motors to be straigth
            k = {1: 510, 2: 510, 3: 820}
            # Send the command to the motors
            interface.update_motors(k)
            # Wait to be sure the motors have done the command
            time.sleep(0.5)
            print("Avaible commands : hello, walkf, walkb")
            command = input("Put a command : ")
            if command in commands:
                commands[command]()
            else:
                print("Command not found")

    else:
        print("No motors founds")

    interface.close()

# Command to say hello
def hello_command(interface):
    # Max range for my motors 3
    k = {3: 1020}
    interface.update_motors(k)
    time.sleep(0.5)
    # Max range for my motors 1
    k = {1: 810}
    interface.update_motors(k)
    time.sleep(0.2)
    for i in range(3):
        # Min range for my motors 1
        k = {1: 210}
        interface.update_motors(k)
        time.sleep(0.4)
        # Max range for my motors 1
        k = {1: 810}
        interface.update_motors(k)
        time.sleep(0.4)

# Command to walk forward like a spider
def walkf_command(interface):
    # Start position
    k = {1: 510, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(1)

    # Up the leg
    k = {1: 510, 2: 510, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.2)

    # Forward
    k = {1: 360, 2: 510, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.3)

    # Down the leg
    k = {1: 360, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(0.2)

    # Backward
    k = {1: 660, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(0.5)

    for i in range(5):
        # Up the leg
        k = {1: 660, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.2)

        # Forward
        k = {1: 360, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.5)

        # Down the leg
        k = {1: 360, 2: 685, 3: 960}
        interface.update_motors(k)
        time.sleep(0.2)

        # Backward
        k = {1: 660, 2: 685, 3: 960}
        interface.update_motors(k)
        time.sleep(0.5)

# Command to walk backward like a spider
def walkb_command(interface):
    # Start position
    k = {1: 510, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(1)

    # Up the leg
    k = {1: 510, 2: 510, 3: 960}
    interface.update_motors(k)
    time.sleep(0.2)

    # Backward
    k = {1: 660, 2: 510, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.3)

    # Down the leg
    k = {1: 660, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(0.2)

    # Forward 
    k = {1: 360, 2: 685, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.5)

    for i in range(5):
        # Up the leg
        k = {1: 360, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.2)

        # Backward
        k = {1: 660, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.5)

        # Down the leg
        k = {1: 660, 2: 685, 3: 960}
        interface.update_motors(k)
        time.sleep(0.2)

        # Forward
        k = {1: 360, 2: 685, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.5)


if __name__ == "__main__":
    main()

