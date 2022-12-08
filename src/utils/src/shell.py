from .cprint import cprint

def execute(command_args, return_output=False):
    import subprocess
    if is_running_on_ubuntu():
        if return_output is True:
            output = subprocess.check_output(command_args)
            return output
        else:
            error_code = subprocess.Popen(command_args).wait()
            return error_code
    else:
        from termcolor import colored
        msg = f"Skipping execution of command `{command_args}`"
        cprint(msg, "yellow", indent=1)


def is_installed_executable(command):
    """Check whether `command` is on PATH and marked as executable."""
    from shutil import which
    return which(command) is not None


def is_running_on_ubuntu():
    import platform
    return 'ubuntu' in platform.version().lower()


def user_does_exist(user):
    import pwd
    try:
        pwd.getpwnam(user)
    except KeyError:
        return False
    return True


def get_ip_address():
    address = execute(["hostname", "-I"], return_output=True)
    if address != None:
        address = str(address)
        address = address[2:] if address.startswith("b'") else address
        address = address.split(" ")[0]
        return address
    else:
        return "127.0.0.1"

