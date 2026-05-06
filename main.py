import time
import keyboard
from colorama import Fore, Style, init
    
init(autoreset=True)

START_KEY = "i"
STOP_KEY = "q"
STARTUP_DELAY = 2  # seconds
KEY_PRESS_DURATION = 0.1  # seconds
DEFAULT_KEY = "space"
DEFAULT_INTERVAL = 1  # seconds

print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}" + r"""
  /$$   /$$                     /$$                                    
| $$  /$$/                    | $$                                    
| $$ /$$/   /$$$$$$  /$$   /$$| $$        /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$/   /$$__  $$| $$  | $$| $$       /$$__  $$ /$$__  $$ /$$__  $$
| $$  $$  | $$$$$$$$| $$  | $$| $$      | $$  \ $$| $$  \ $$| $$  \ $$
| $$\  $$ | $$_____/| $$  | $$| $$      | $$  | $$| $$  | $$| $$  | $$
| $$ \  $$|  $$$$$$$|  $$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$/
|__/  \__/ \_______/ \____  $$|________/ \______/  \______/ | $$____/ 
                     /$$  | $$                              | $$      
                    |  $$$$$$/                              | $$      
                     \______/                               |__/        
""" + f"{Style.RESET_ALL}")

print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to KeyLoop{Style.RESET_ALL}\n")

key_input = input(f"{Fore.YELLOW}Enter the key you want to press (default is spacebar): {Style.RESET_ALL}")
key = key_input if key_input else DEFAULT_KEY

interval_input = input(f"{Fore.YELLOW}Enter the time between presses in seconds (default is 1): {Style.RESET_ALL}")
try:
    time_between_presses = float(interval_input) if interval_input else DEFAULT_INTERVAL
except ValueError:
    print(f"{Fore.RED}{Style.BRIGHT}Invalid input for time interval. Using default value of {DEFAULT_INTERVAL} seconds.{Style.RESET_ALL}")
    time_between_presses = DEFAULT_INTERVAL

stop_macro: bool = False
macro_running: bool = False


def start_stop_macro_function() -> None:
    global macro_running
    macro_running = not macro_running
    if macro_running:
        print(f"{Fore.GREEN}{Style.BRIGHT}Macro started.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}{Style.BRIGHT}Macro paused.{Style.RESET_ALL}")


def stop_macro_function() -> None:
    global stop_macro, macro_running
    stop_macro = True
    macro_running = False
    print(f"{Fore.RED}{Style.BRIGHT}Macro stopped.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}Thank you for using KeyLoop!{Style.RESET_ALL}")


keyboard.add_hotkey(START_KEY, start_stop_macro_function, suppress=True)
keyboard.add_hotkey(STOP_KEY, stop_macro_function, suppress=True)

time.sleep(STARTUP_DELAY)


def press_key() -> None:
    global stop_macro, macro_running
    try:
        print(f"{Fore.GREEN}{Style.BRIGHT}Press '{START_KEY}' to start the macro.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}Press '{STOP_KEY}' to exit.{Style.RESET_ALL}\n")
        
        while not stop_macro:
            if macro_running:
                keyboard.press(key)
                time.sleep(KEY_PRESS_DURATION)
                keyboard.release(key)
                if not stop_macro:
                    time.sleep(time_between_presses)
            else:
                time.sleep(0.1)  # Small sleep to avoid high CPU usage
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}{Style.BRIGHT}Macro interrupted.{Style.RESET_ALL}")


if __name__ == "__main__":
    press_key()