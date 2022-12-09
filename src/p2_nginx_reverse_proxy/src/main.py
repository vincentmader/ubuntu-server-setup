import os

import config as cfg
from utils.cprint import cprint
from utils.cprint import cprint_header
from utils.shell import execute
from utils.shell import get_ip_address
from utils.shell import is_running_on_ubuntu


def install_nginx():
    cprint("Installing Nginx...", indent=1)
    execute(["apt", "-y", "install", "nginx"])


def configure_nginx_firewall_access():
    cprint("Configuring Nginx firewall access...", indent=1)
    execute(["ufw", "allow", "Nginx HTTP"])
    execute(["systemctl", "status", "nginx"])


def create_nginx_server_block(address, domain):
    cprint("Creating Nginx server block...", indent=1)
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
    return content


def save_nginx_server_block(content):
    cprint("Saving Nginx server block to file...", indent=1)
    if is_running_on_ubuntu():
        path_to_file = f"/etc/nginx/sites-available/{domain}"
        with open(path_to_file, 'w') as fp:
            fp.write(content)


def enable_site(domain):
    cprint("Enabling site...", indent=1)
    sites_available = f"/etc/nginx/sites-available/"
    sites_enabled = f"/etc/nginx/sites-enabled/"
    site = os.path.join(sites_available, domain)
    if not os.path.exists(sites_enabled):
        execute(["ln", "-s", site, sites_enabled])


if __name__ == "__main__":
    cprint_header("Part 2: Nginx Reverse Proxy")

    install_nginx()
    configure_nginx_firewall_access()

    domain = cfg.DOMAIN
    address = get_ip_address()
    server_block = create_nginx_server_block(address, domain)
    save_nginx_server_block(server_block)

    enable_site(domain)
