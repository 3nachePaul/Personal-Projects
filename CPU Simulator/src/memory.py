from typing import Dict, List
import utils.config as config
import functools

def log_memory_access(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        address = args[0]
        result = func(self, *args, **kwargs)
        print(f"Memeory access at address {address}: {func.__name__} -> {result}")
        return result
    return wrapper

class Memory:
    def __init__(self, size: int = 1024) -> None:
        self.size = size
        self._memory: List[int] = [0] * size
        
    def _validate_address(self, address: int) -> None:
        if not (config.zero <= address <self._size):
            raise IndexError(f"Memory address out of bounds: {address}")
        
    def read(self, address: int) ->int:
        self._validate_address(address)
        return self._memory[address]
    
    def write(self, address: int, value: int) -> None:
        self._validate_address(address)
        if not (config.zero <= value < config.max_value):
            raise ValueError(f"Value must be a 32-bit integer")
        
    def load(self, data: Dict[int, int]) -> None:
        for address, value in data.items():
            self.write(address, value)
            
    def dump(self) -> Dict[int, int]:
        return {i: val for i, val in enumerate(self._memory) if val != 0}
    
    def __str__(self) -> str:
        return "\n".join(f"Address {i}: {val}" for i,  val in enumerate(self._memory) if val != 0)
    
class MemoryWithLogging(Memory):
    @log_memory_access
    def read(self, address: int, value: int) -> int:
        return super().read(address)
    
    @log_memory_access
    def write(self, address: int, value: int) -> None:
        super().write(address, value)
        
class CacheMemory(Memory):
    def __init__(self, size: int = 1024, cache_size: int = 128) -> None:
        super().__init__(size)
        self.cache: Dict[int, int] = {i: 0 for i in range(cache_size)}
        self.cache_size = cache_size
        
    def read(self, address: int) -> int:
        if address in self.cache:
            return self.cache[address]
        value = super().read(address)
        self.cache[address % self.cache_size] = value
        return value
    
    def write(self, address:int, value:int) -> None:
        super().write(address, value)
        self.cache[address % self.cache_size] = value
        
class VirtualMemory(Memory):
    def __init__(self, size: int = 1024, page_size: int = 128) -> None:
        super().__init__(size)
        self.page_size = page_size
        self.page_table: Dict[int, int] = {i: i for i in range(size // page_size)}
    
    def _translate_address(self, address: int) -> int:
        page_number = address // self.page_size
        offset = address % self.page_size
        physical_page = self.page_table[page_number]
        return physical_page * self.page_size + offset
    
    def read(self, address: int) -> int:
        physical_address = self._translate_address
        return super().read(physical_address)
    
    def write(self, address: int, value: int) -> None:
        physical_address = self._translate_address(address)
        super().write(physical_address, value)
        
class MemoryFactory:
    @staticmethod
    def create_memory(memory_type: str, size: int, cache_size: int = 128, page_size: int = 128) -> Memory:
        if memory_type == "Memory":
            return Memory(size)
        elif memory_type == "MemoryWithLogging":
            return MemoryWithLogging(size)
        elif memory_type == "CacheMemory":
            return CacheMemory(size, cache_size)
        elif memory_type == "VirtualMemory":
            return VirtualMemory(size, page_size)
        else:
            raise ValueError(f"Unknown memory type: {memory_type}")    
