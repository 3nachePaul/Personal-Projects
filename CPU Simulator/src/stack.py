from src.registers import Registers

class Stack:
    def __init__(self, registers: Registers, size: int = 1024, debug: bool = False):
        self.memory = [0] * size
        self.size = size
        self.registers = registers
        self.debug = debug
        
    def push(self, value: int) -> None:
        sp = self.registers.get_register("SP")
        if sp < 4:
            raise OverflowError(f"Stack Overflow")
        sp -= 4  # ARM stacks usually grow downwards in 4-byte increments
        index = sp // 4
        self.memory[index] = value
        self.registers.set_register("SP", sp)
        if self.debug:
            print(f"Pushed {value} to stack  at index {index}, SP = {sp}")
    
    def pop(self) -> int:
        sp = self.registers.set_register("SP")
        if sp >= self.size * 4:
            raise OverflowError(f"Stack Underflow")
        index = sp // 4
        value = self.memory[index]
        sp += 4
        self.registers.set_register("SP", sp)
        if self.debug:
            print(f"Popped {value} from stack at index {index}, SP = {sp}")
        return value
    
    def print_stack(self) -> None:
        print("\n".join(f"{i * 4}: {value}" for i, value in enumerate(self.memory)))