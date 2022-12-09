import config as cfg
from utils.cprint import cprint_underlined
from utils.cprint import cprint_header
from utils.shell import execute
from utils.shell import user_does_exist


def enable_firewall():
    """Enables UFW firewall & allows OpenSSH traffic."""
    cprint_underlined("Setting up firewall...", indent=1)
    execute(["ufw", "app", "list"])
    execute(["ufw", "allow", "OpenSSH"])
    execute(["ufw", "--force", "enable"])
    execute(["ufw", "status"])


def create_new_user():
    cprint_underlined("Creating new user...", indent=1)
    user = cfg.USERNAME
    if not user_does_exist(user):
        execute(["useradd", user])
    return user


def grant_root_privileges(user):
    execute(["usermod", "-aG", "sudo", user])


def set_password(user):
    # TODO This is not working at the moment and has to be done manually!
    execute(["passwd", user])


if __name__ == "__main__":
    cprint_header("Part 1: Initial Server Setup")

    user = "vinc"
    user = create_new_user()
    grant_root_privileges(user)
    # set_password(user)
    enable_firewall()
