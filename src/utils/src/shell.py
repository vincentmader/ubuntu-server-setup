def execute(command):
    import subprocess
    if is_running_on_ubuntu():
        subprocess.Popen(command)
    else:
        from termcolor import colored
        msg = f"Skipping execution of command `{command}`..."
        msg = colored(msg, "yellow")
        print(msg)


def is_installed_executable(command):
    """Check whether `command` is on PATH and marked as executable."""
    from shutil import which
    return which(command) is not None


def is_running_on_ubuntu():
    import platform
    return 'ubuntu' in platform.version().lower()
