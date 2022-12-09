import os

import config as cfg
from utils.cprint import cprint
from utils.cprint import cprint_underlined
from utils.cprint import cprint_header
from utils.shell import execute
from utils.shell import get_ip_address
from utils.shell import is_running_on_ubuntu


def install_nginx():
    cprint_underlined("Installing Nginx...")
    execute(["apt", "-y", "install", "nginx"])


def configure_nginx_firewall_access():
    cprint_underlined("Configuring Nginx firewall access...")
    execute(["ufw", "allow", "Nginx HTTP"])


def create_nginx_server_block(address, domain):
    cprint_underlined("Creating Nginx server block...")
    content = "server {"
    content += "\n    listen 80;"
    content += "\n    listen [::]:80;"
    content += "\n"
    content += "\n    server_name {} www.{};".format(domain, domain)
    content += "\n"
    content += "\n    location / {"
    content += "\n        proxy_pass http://{};".format(address)
    content += "\n        include proxy_params;"
    content += "\n    }"
    content += "\n}"
    for line in content.split("\n"):
        cprint(line)
    return content


def save_nginx_server_block(content):
    cprint_underlined("Saving Nginx server block to file...")
    if is_running_on_ubuntu():
        path_to_file = f"/etc/nginx/sites-available/{domain}"
        with open(path_to_file, 'w') as fp:
            fp.write(content)
        cprint("Saved Nginx server block.", color="green")


def enable_site(domain):
    cprint_underlined("Enabling site...")
    sites_available = f"/etc/nginx/sites-available/"
    sites_enabled = f"/etc/nginx/sites-enabled/"
    site = os.path.join(sites_available, domain)
    if not os.path.exists(sites_enabled):
        execute(["ln", "-s", site, sites_enabled])
    cprint("Site is enabled.", color="green")


if __name__ == "__main__":
    cprint_header("Part 2: Nginx Reverse Proxy")

    install_nginx()
    configure_nginx_firewall_access()

    domain = cfg.DOMAIN
    address = get_ip_address()
    server_block = create_nginx_server_block(address, domain)
    save_nginx_server_block(server_block)

    enable_site(domain)
    print()
