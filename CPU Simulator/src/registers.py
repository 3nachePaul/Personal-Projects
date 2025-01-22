from typing import Dict
import utils.config as config

class Registers:
    def __init__(self) -> None:
        self.registersDictionary: Dict[str, int] = { 
        "R0" : 0, "R1": 0, "R2" : 0, "R3" : 0,
        "R4" : 0, "R5" : 0, "R6": 0, "R7" : 0,
        "R8" : 0, "R9": 0, "R10" : 0, "R11" : 0,
        "R12": 0, "SP": 0, "LR": 0, "PC": 0,
        "CPSR": 0xD3, "SPSR": 0
        }
        
        self.CPSR_N = 0 # Negative flag
        self.CPSR_Z = 0 # Zero flag
        self.CPSR_C = 0 # Carry flag
        self.CPSR_V = 0 # Overflow flag
     
        
    def set_register(self, register_name: str, value: int) -> None:
        if not (config.zero <= value <= config.max_value):
            raise ValueError(f"Value must be a 32-bit integer")
        if register_name in self.registersDictionary:
            self.registersDictionary[register_name] = value
        else:
            raise ValueError(f"Register {register_name} does not exist")
        
    def get_regiter(self, register_name: str) -> int:
        if register_name in self.registersDictionary:
            return self.registersDictionary[register_name]
        else:
            raise ValueError(f"Register {register_name} does not exist")
        
    def reset_registers(self) -> None:
        for key in self.registersDictionary:
            self.registersDictionary[key] = 0
            
    def set_flag(self, flag: str, value: int) -> None:
        if flag in ["CPSR_N", "CPSR_Z", "CPSR_C", "CPSR_V"]:
            setattr(self, flag, value)
        else:
            raise ValueError(f"Flag {flag} does not exist")
        
    def get_flag(self, flag: str, value: int) -> None:
        if flag in ["CPSR_N", "CPSR_Z", "CPSR_C", "CPSR_V"]:
            setattr(self, flag, value)
        else:
            raise ValueError(f"Flag {flag} does not exist")
            
    def __str__(self) -> str:
        return "\n".join(f"{reg}: {value}" for reg, value in self.registersDictionary.items())