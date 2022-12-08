from utils.cprint import cprint
from utils.shell import execute


def install_nginx():
    execute(["apt", "install", "nginx"])


if __name__ == "__main__":
    cprint("Part 2: Nginx Reverse Proxy", color="blue", newline=True)

    install_nginx()
