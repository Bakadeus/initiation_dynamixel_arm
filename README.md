## Robotic Arm Project

This project controls a robotic arm with 3 degrees of freedom using a Raspberry
Pi and Python.

#### Installation

Clone the repository:

```bash
git clone https://github.com/Bakadeus/initiation_dynamixel_arm.git
```

Navigate into the project directory:

```bash
cd initiation_dynamixel_arm
```

Install dependencies:

```bash
pip install -r requirements.txt
```

This will install the required Python package, "Dynamixel_SDK"

#### Usage

To start controlling the arm, run:

```bash
python main.py
```

This will open the main function to play with the arm.

Press Ctrl+C to exit arm control mode.

Architecture

*   arm_control.py - Main script, initializes GPIO pins, servos, and enters control loop
*   servo.py - Contains Servo class to control angle/speed of a servo
*   gripper.py - Contains Gripper class to control gripper open/close state
*   ik.py - Contains inverse kinematics functions to calculate joint angles
*   pid.py - Implementation of a PID controller for stable servo positioning