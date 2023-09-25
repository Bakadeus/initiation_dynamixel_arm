## Robotic Arm Project

This project controls a robotic arm with 3 degrees of freedom using a Raspberry
Pi and Python.

#### Architecture

    *   Dynamixel/
        *   constants.py - Config all variable
        *   ctrl_table.py - Config motors file
        *   exceptions.py - Model to handle exceptions
        *   interface.py - Interface for the motors
        *   servo.py - All function to interact with the motors
    *   main.py - Test file to start play with the arm
    *   requirements.txt - All the requirements

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

Press Ctrl+C to exit main function.

