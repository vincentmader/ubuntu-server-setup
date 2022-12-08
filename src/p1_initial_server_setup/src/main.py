from utils.cprint import cprint
from utils.shell import execute

def create_new_user():
    cprint("Creating new user...", indent=1)
    cprint("Username: ", end="", indent=1)
    username = input()
    execute(f"useradd {username}")

if __name__ == "__main__":
    cprint("Part 1: Initial Server Setup", color="blue", newline=True)

    create_new_user()
