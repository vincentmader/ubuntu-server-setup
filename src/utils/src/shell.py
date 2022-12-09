from .cprint import cprint


def execute(command_args, check_output=False):
    if not is_running_on_ubuntu():
        cprint(f"Skipping `{' '.join(command_args)}`", "yellow", indent=1)
        return None

    import subprocess
    if check_output is True:
        output = subprocess.check_output(command_args)
        return output
    else:
        error_code = subprocess.Popen(command_args).wait()
        return error_code


def is_installed_executable(command):
    """Checks whether `command` is on PATH and marked as executable."""
    from shutil import which
    return which(command) is not None


def is_running_on_ubuntu():
    """Checks whether host machine is running Ubuntu (>14.04)."""
    import platform
    return 'ubuntu' in platform.version().lower()


def user_does_exist(user):
    """Checks whether `user` exists on host machine."""
    import pwd
    try:
        pwd.getpwnam(user)
        return True
    except KeyError:
        return False


def get_ip_address():
    """Determines IP address of host machine."""
    address = execute(["hostname", "-I"], check_output=True)
    if type(address) is str:
        return address.decode("utf-8").split(" ")[0]
    else:
        return None
