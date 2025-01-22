from typing import Dict
from registers import Registers
from bus import MemoryBus

class CPU:
    def __init__(self, memory_type: str = "Memory", memory_size: int = 1024, cache_size: int = 128, page_size: int = 128) -> None:
        self.registers = Registers()
        self.memory_bus = MemoryBus(memory_type, memory_size, cache_size, page_size)
        self.opcode_map = {
            0x01: self.mov,
            0x02: self.add,
            0x03: self.sub,
            0x04: self.and_op,
            0x05: self.orr,
            0x06: self.branch,
        }

    def fetch(self) -> int:
        pc = self.registers.get_register("PC")
        instruction = self.memory_bus.read(pc)
        self.registers.set_register("PC", pc + 4)  # Increment PC after fetching
        return instruction

    def decode(self, instruction: int) -> Dict[str, int]:
        return {
            "opcode": (instruction >> 24) & 0xFF,
            "operand1": (instruction >> 16) & 0xFF,
            "operand2": (instruction >> 8) & 0xFF,
            "operand3": instruction & 0xFF
        }

    def execute(self, decoded_instruction: Dict[str, int]) -> None:
        opcode = decoded_instruction["opcode"]
        if opcode in self.opcode_map:
            self.opcode_map[opcode](decoded_instruction)
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    def mov(self, decoded_instruction: Dict[str, int]) -> None:
        operand1 = decoded_instruction["operand1"]
        operand2 = decoded_instruction["operand2"]
        self.registers.set_register(f"R{operand1}", operand2)

    def add(self, decoded_instruction: Dict[str, int]) -> None:
        operand1 = decoded_instruction["operand1"]
        operand2 = decoded_instruction["operand2"]
        result = self.registers.get_register(f"R{operand1}") + self.registers.get_register(f"R{operand2}")
        self.registers.set_register(f"R{operand1}", result)
        self.update_flags(result)

    def sub(self, decoded_instruction: Dict[str, int]) -> None:
        operand1 = decoded_instruction["operand1"]
        operand2 = decoded_instruction["operand2"]
        result = self.registers.get_register(f"R{operand1}") - self.registers.get_register(f"R{operand2}")
        self.registers.set_register(f"R{operand1}", result)
        self.update_flags(result)

    def and_op(self, decoded_instruction: Dict[str, int]) -> None:
        operand1 = decoded_instruction["operand1"]
        operand2 = decoded_instruction["operand2"]
        result = self.registers.get_register(f"R{operand1}") & self.registers.get_register(f"R{operand2}")
        self.registers.set_register(f"R{operand1}", result)
        self.update_flags(result)

    def orr(self, decoded_instruction: Dict[str, int]) -> None:
        operand1 = decoded_instruction["operand1"]
        operand2 = decoded_instruction["operand2"]
        result = self.registers.get_register(f"R{operand1}") | self.registers.get_register(f"R{operand2}")
        self.registers.set_register(f"R{operand1}", result)
        self.update_flags(result)

    def branch(self, decoded_instruction: Dict[str, int]) -> None:
        operand1 = decoded_instruction["operand1"]
        self.registers.set_register("PC", self.registers.get_register(f"R{operand1}"))

    def update_flags(self, result: int) -> None:
        self.registers.set_flag("CPSR_N", 1 if result < 0 else 0)
        self.registers.set_flag("CPSR_Z", 1 if result == 0 else 0)
        self.registers.set_flag("CPSR_C", 1 if (result & 0x100000000) != 0 else 0)  # Carry out check
        self.registers.set_flag("CPSR_V", 1 if result > 0x7FFFFFFF or result < -0x80000000 else 0)


    def run(self) -> None:
        while True:
            instruction = self.fetch()
            decoded_instruction = self.decode(instruction)
            self.execute(decoded_instruction)

    def reset(self) -> None:
        self.registers.reset_registers()
        self.memory_bus.reset()
        

    def print_cpu_state(self) -> None:
        print("CPU State:")
        print(self.registers)
        self.memory_bus.print_memory_state()