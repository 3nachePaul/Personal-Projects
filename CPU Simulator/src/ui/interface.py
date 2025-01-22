from utils.cpu_interaction import get_cpu_usage, set_cpu_parameters
from cpu import CPU

class UserInterface:
    def __init__(self):
        self.cpu = CPU()

    def display_menu(self):
        print("CPU Interaction Menu:")
        print("1. Get CPU Usage")
        print("2. Set CPU Parameters")
        print("3. Exit")

    def get_user_input(self):
        choice = input("Please select an option (1-3): ")
        return choice

    def handle_choice(self, choice):
        if choice == '1':
            print(f"CPU Usage: {get_cpu_usage()}%")
        elif choice == '2':
            param = input("Enter parameter to set: ")
            value = input("Enter value: ")
            set_cpu_parameters(param, value)
            print("Parameter set successfully.")
        elif choice == '3':
            print("Exiting...")
            return False
        else:
            print("Invalid choice. Please try again.")
        return True

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_input()
            if not self.handle_choice(choice):
                break