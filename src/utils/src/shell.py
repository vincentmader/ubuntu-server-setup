from .cprint import cprint

def execute(command):
    import subprocess
    if is_running_on_ubuntu():
        subprocess.Popen(command).wait()
    else:
        from termcolor import colored
        msg = f"Skipping execution of command `{command}`"
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
