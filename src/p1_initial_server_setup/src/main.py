from utils.cprint import cprint
from utils.shell import execute

def create_new_user():
    cprint("Creating new user...", indent=1)
    cprint("Username: ", end="", indent=1)
    user = input()
    execute(["useradd", user])
    return user


def grant_root_privileges(user):
    execute(["usermod", "-aG", "sudo", user])


def set_password(user):
    execute(["passwd", user])


if __name__ == "__main__":
    cprint("Part 1: Initial Server Setup", color="blue", newline=True)

    user = create_new_user()
    grant_root_privileges(user)
    set_password(user)
