from PCB import PCB
import Process_And_Helping_Functions as library


def add_process(table):
    pid = library.is_in_dictionary(library.check_if_digit(library.try_input("Enter PID: ")), table)
    registers = {}
    while True:
        name = library.try_input("Register name (Enter to stop): ")
        if not name:
            break
        value = library.check_if_digit(library.try_input("Value: "))
        registers[name] = value

    table[pid] = PCB(pid, registers)
    print("Process added successfully.")
    return


def view_process(table):
    pid = library.check_if_digit(library.try_input("Enter PID to view: "))
    if pid in table:
        print(table[pid])
    else:
        print("PID not found.")
    return


def print_all_processes(table):
    if not table:
        print("No processes found.")
    for pcb in table.values():
        print(pcb)
    return


def print_menu() -> None:
    print(" 1) Adding A Process\n 2) View Process \n 3) Print All Processes \n 4) Exit.")
    return


def main():
    table = {}
    while True:
        print_menu()
        choice = library.check_if_digit(library.try_input("Choose an option: "))
        if choice == 1:
            add_process(table)
        elif choice == 2:
            view_process(table)
        elif choice == 3:
            print_all_processes(table)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
main()



