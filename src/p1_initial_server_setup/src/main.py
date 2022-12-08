from time import sleep

from utils.cprint import cprint
from utils.shell import execute
from utils.shell import user_does_exist


def enable_firewall():
    execute(["ufw", "app", "list"])
    execute(["ufw", "allow", "OpenSSH"])
    execute(["ufw", "enable"])
    execute(["ufw", "status"])
    sleep(1)


def create_new_user():
    cprint("Creating new user...", indent=1)
    cprint("Username: ", end="", indent=1)
    user = input()
    if not user_does_exist(user):
        execute(["useradd", user])
    return user


def grant_root_privileges(user):
    execute(["usermod", "-aG", "sudo", user])


def set_password(user):
    # TODO This is not working at the moment and has to be done manually!
    execute(["passwd", user])


if __name__ == "__main__":
    cprint("Part 1: Initial Server Setup", color="blue", newline=True)

    user = "vinc"
    user = create_new_user()
    grant_root_privileges(user)
    # set_password(user)
    enable_firewall()
