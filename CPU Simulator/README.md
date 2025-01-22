# CPU Simulator

This project is a Python program designed to simulate a CPU. It provides an interface for interacting with the CPU, including getting CPU usage and setting CPU parameters. The project is still under development and is not yet finished.

## Project Structure

```bash
src
    │   bus.py
    │   cpu.py
    │   main.py
    │   memory.py
    │   registers.py
    │   stack.py
    │   
    ├───ui
    │   │   interface.py
    │   │
    │   └───__pycache__
    │           interface.cpython-311.pyc
    │
    ├───utils
    │   │   config.py
    │   │   cpu_interaction.py
    │   │   functions.py
    │   │
    │   └───__pycache__
    │           config.cpython-311.pyc
    │           cpu_interaction.cpython-311.pyc
    │
    └───__pycache__
            bus.cpython-311.pyc
            cpu.cpython-311.pyc
            memory.cpython-311.pyc
            registers.cpython-311.pyc

```


### Explanation of the Structure

- **src/main.py**: This is the entry point for the application. It initializes the user interface and starts the interaction loop.

- **src/ui/interface.py**: This file contains the user interface code. It provides a menu for interacting with the CPU, including options to get CPU usage and set CPU parameters.

- **src/utils/cpu_interaction.py**: This file contains utility functions for CPU interaction, such as getting CPU usage and setting CPU parameters.

- **src/cpu.py**: This file defines the `CPU` class and related functions. It simulates the CPU's behavior, including loading and running programs.

- **src/bus.py**: This file defines the `MemoryBus` class and related functions. It handles memory operations and interactions with the CPU's registers.

- **src/memory.py**: This file defines the `Memory` class and related functions. It manages the memory operations for the CPU simulation.

- **src/registers.py**: This file defines the `Registers` class and related functions. It manages the CPU's registers, including general-purpose and special-purpose registers.

- **src/stack.py**: This file defines the `Stack` class and related functions. It manages the stack operations, including push and pop operations, for the CPU simulation.

### How to Run

1. Clone the repository to your local machine.
2. Navigate to the `src` directory.
3. Run the `main.py` file using Python:

### Requirements
-Python 3.x
-psutil library (for getting CPU usage)

### Installation
Install the required dependencies using pip:   ```pip install psutil```

## Note
This project is a work in progress and is not yet finished. Contributions and suggestions are welcome!