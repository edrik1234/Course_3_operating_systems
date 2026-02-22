from Process_States import Process_State


def check_if_digit(value) -> int:
    while not value.isdigit(): 
        print("The value: " + str(value) + " isn't a number please try again")
        value = input("Enter a valid value: ")  
    return int(value)   


def try_input(prompt: str) -> str | None :
    try:
        input_value = input(prompt)
        return input_value
    except KeyboardInterrupt:
        print("you have pressed ctrl + c we are now exiting")
        return None
    

def check_if_alpha(user_input: str) -> str:
    while not user_input.isalpha():
        print("this input  isn't a string try to type again please")
        user_input = try_input("please enter again and please enter a correct string: ").strip()
    return str(user_input)


def is_in_dictionary(key, dictionary) -> int:
    while key in dictionary:
        print("the value is in dictionary please type pid again: ")
        key = check_if_digit(try_input("please enter a normal value: "))
    return key


def check_process_states(input_process) -> str | None:
    while True:
        for state in Process_State:
            if input_process == state.name:
                print("the process state is ok")
                return str(input_process)
        else:
            print("invalid process state please try again")
            input_process = check_if_alpha(try_input("please enter a process state: ").strip())
        


def input_files() -> list[str]:
    files_input = try_input("please enter name of files open in process (like in this format: edrik.txt, toni.csv and etc... ): ")
    open_files = [f.strip() for f in files_input.split(',') if f.strip()]
    return open_files