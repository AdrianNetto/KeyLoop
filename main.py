import time
from typing import NoReturn

import keyboard
from colorama import Fore, Style, init
    
init(autoreset=True)

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


def stop_macro_function() -> None:
    global stop_macro
    stop_macro = True
    print(f"{Fore.RED}{Style.BRIGHT}Macro stopped.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}Thank you for using KeyLoop!{Style.RESET_ALL}")
        

keyboard.add_hotkey(STOP_KEY, stop_macro_function, suppress=True)

time.sleep(STARTUP_DELAY)


def press_key() -> NoReturn:
    global stop_macro
    try:
        print(f"{Fore.GREEN}{Style.BRIGHT}Press '{STOP_KEY}' to stop the macro.{Style.RESET_ALL}")
        while not stop_macro:
            if stop_macro:
                break
            keyboard.press(key)
            time.sleep(KEY_PRESS_DURATION)
            keyboard.release(key)
            if stop_macro:
                break
            time.sleep(time_between_presses)
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}{Style.BRIGHT}Macro interrupted.{Style.RESET_ALL}")


if __name__ == "__main__":
    press_key()