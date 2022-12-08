from utils.cprint import cprint
from utils.shell import execute


def install_nginx():
    execute(["apt", "-y", "install", "nginx"])


def setup_firewall_for_nginx():
    execute(["ufw", "allow", "Nginx HTTP"])


if __name__ == "__main__":
    cprint("Part 2: Nginx Reverse Proxy", color="blue", newline=True)

    install_nginx()
    setup_firewall_for_nginx()
