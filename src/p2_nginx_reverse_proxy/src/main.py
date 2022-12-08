from utils.cprint import cprint
from utils.shell import execute
from utils.shell import get_ip_address


def install_nginx():
    execute(["apt", "-y", "install", "nginx"])


def setup_firewall_for_nginx():
    execute(["ufw", "allow", "Nginx HTTP"])
    execute(["systemctl", "status", "nginx"])


def create_nginx_server_block(domain, ip_address):
    content = ""
    content += "server {\n"
    content += "    listen 80;\n"
    content += "    listen [::]:80;\n"
    content += "\n"
    content += "    server_name {} www.{};\n".format(domain, domain)
    content += "\n"
    content += "    location / {\n"
    content += "        proxy_pass {};\n".format(ip_address)
    content += "        include proxy_params;\n"
    content += "    }\n"
    content += "}"


def get_server_domain_and_address():
    domain = "sonoapp.de"  # TODO Move to config? Get from input?
    ip_address = get_ip_address()
    return domain, ip_address


if __name__ == "__main__":
    cprint("Part 2: Nginx Reverse Proxy", color="blue", newline=True)

    install_nginx()
    setup_firewall_for_nginx()

    domain, ip_address = get_server_domain_and_address()
    nginx_server_block = create_nginx_server_block(domain, ip_address)
