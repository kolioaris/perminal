import os
import shlex
import importlib.util
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    while True:
        try:
            command = input("$ ")
            if command:
                run_command(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' or 'quit' to quit.")
        except EOFError:
            print("\nExiting shell...")
            break

def run_command(command: str):
    args = shlex.split(command)
    command_name = args[0]
    command_file = os.path.join("commands", f"{command_name}.py")
    
    if os.path.isfile(command_file):
        spec = importlib.util.spec_from_file_location(command_name, command_file)
        module = importlib.util.module_from_spec(spec)

        sys.dont_write_bytecode = True  

        spec.loader.exec_module(module)
        module.run(args[1:])
    else:
        print(f"Command not found: {command_name}")

if __name__ == "__main__":
    clear_screen()
    main()