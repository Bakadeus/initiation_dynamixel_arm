#!/usr/bin/python

# https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/

import time
from dynamixel.interface import Interface
from dynamixel.constants import MID_ANGLE, MIN_ANGLE


def say_hello():
    interface = Interface()

    interface.discover()

    for i in interface._motors:
        print(f"Motor #{i} found")

    time.sleep(1)

    servo_01 = interface.get_servo(1)
    servo_02 = interface.get_servo(2)
    servo_03 = interface.get_servo(3)

    if servo_01 and servo_02 and servo_03:

        commands = {
            "coucou": lambda: coucou_command(interface),
            "walkf": lambda: walkf_command(interface),
            "walkb": lambda: walkb_command(interface)
        }

        while True:
            k = {1: 510, 2: 510, 3: 820}
            interface.update_motors(k)
            time.sleep(0.5)
            print("Commandes disponibles : coucou, walkf, walkb")
            command = input("Entrez une commande : ")
            if command in commands:
                commands[command]()  # Exécute la fonction associée à la commande
            else:
                print("Commande non reconnue")

    else:
        print("No motors founds")

    interface.close()


def coucou_command(interface):
    k = {3: 1020}
    interface.update_motors(k)
    time.sleep(0.5)
    k = {1: 810}
    interface.update_motors(k)
    time.sleep(0.2)
    for i in range(3):
        k = {1: 210}
        interface.update_motors(k)
        time.sleep(0.4)
        k = {1: 810}
        interface.update_motors(k)
        time.sleep(0.4)


def walkf_command(interface):
    # Start une patte
    k = {1: 510, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(1)

    # Lève la patte
    k = {1: 510, 2: 510, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.2)

    # Avance
    k = {1: 360, 2: 510, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.3)

    # Baisse la patte
    k = {1: 360, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(0.2)

    # Recule
    k = {1: 660, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(0.5)

    for i in range(5):
        # Lève la patte
        k = {1: 660, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.2)

        # Avance
        k = {1: 360, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.5)

        # Baisse la patte
        k = {1: 360, 2: 685, 3: 960}
        interface.update_motors(k)
        time.sleep(0.2)

        # Recule
        k = {1: 660, 2: 685, 3: 960}
        interface.update_motors(k)
        time.sleep(0.5)

def walkb_command(interface):
    # Start une patte
    k = {1: 510, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(1)

    # Lève la patte
    k = {1: 510, 2: 510, 3: 960}
    interface.update_motors(k)
    time.sleep(0.2)

    # Recule
    k = {1: 660, 2: 510, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.3)

    # Baisse la patte
    k = {1: 660, 2: 685, 3: 960}
    interface.update_motors(k)
    time.sleep(0.2)

     # Avance
    k = {1: 360, 2: 685, 3: 1020}
    interface.update_motors(k)
    time.sleep(0.5)

    for i in range(5):
        # Lève la patte
        k = {1: 360, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.2)

        ## Recule
        k = {1: 660, 2: 510, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.5)

        # Baisse la patte
        k = {1: 660, 2: 685, 3: 960}
        interface.update_motors(k)
        time.sleep(0.2)

        # Avance
        k = {1: 360, 2: 685, 3: 1020}
        interface.update_motors(k)
        time.sleep(0.5)


if __name__ == "__main__":
    say_hello()

