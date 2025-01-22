from typing import Dict
from memory import Memory, MemoryWithLogging, CacheMemory, VirtualMemory, MemoryFactory
from registers import Registers
import utils.config


class MemoryBus:
    def __init__(self, memory_type: str = "Memory", size: int = 1024, cache_size: int = 128, page_size: int = 128) -> None:
        self.memory = MemoryFactory.create_memory(memory_type, size, cache_size, page_size)
        self.registers = Registers()

    def read(self, address: int) -> int:
        return self.memory.read(address)

    def write(self, address: int, value: int) -> None:
        self.memory.write(address, value)

    def load(self, data: Dict[int, int]) -> None:
        self.memory.load(data)

    def dump(self) -> Dict[int, int]:
        return self.memory.dump()

    def __str__(self) -> str:
        return str(self.memory)

    def reset(self) -> None:
        self.memory = MemoryFactory.create_memory(self.memory_type, self.size, self.cache_size, self.page_size)
        self.registers.reset_registers()

    def get_registers(self) -> str:
        return str(self.registers)

    def set_register(self, register_name: str, value: int) -> None:
        self.registers.set_register(register_name, value)

    def get_register(self, register_name: str) -> int:
        return self.registers.get_register(register_name)

    def print_memory_state(self) -> None:
        print("Memory State:")
        print(self)
        print("Registers State:")
        print(self.get_registers())