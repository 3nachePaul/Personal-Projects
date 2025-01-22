from src.cpu import CPU
from typing import Dict


def load_program(cpu: CPU, program: Dict[int, int]) -> None:
    cpu.memory_bus.load(program)

def run_program(cpu: CPU) -> None:
    cpu.run()

def reset_cpu(cpu: CPU) -> None:
    cpu.reset()

def print_cpu_state(cpu: CPU) -> None:
    cpu.print_cpu_state()
