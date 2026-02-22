import Process_And_Helping_Functions as library


class PCB:
    def __init__(self, process_id, registers):
        self.pid = process_id
        self.state = library.check_process_states(library.check_if_alpha(library.try_input("please enter the process state: ").strip())) # i changed here that i removed .capitalize() the main reason is the same as in process and helping functions
        self.program_counter = library.check_if_digit(library.try_input("please enter program counter: "))
        self.memory_start = library.check_if_digit(library.try_input("please enter memory start: "))
        self.memory_end = library.check_if_digit(library.try_input("please enter memory end: "))
        self.registers = registers if registers else {} 
        self.open_files = library.input_files()
    
           

    def __str__(self):
        return (f"PID: {self.pid} | State: {self.state} | Program Counter: {self.program_counter} | "
                f"Memory: {self.memory_start}-{self.memory_end} | Registers: {self.registers} | "
                f"Open Files: {self.open_files}")
      