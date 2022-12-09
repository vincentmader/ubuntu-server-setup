import os

from termcolor import colored


def cprint(text, color="cyan", indent=0, newline=False, end="\n"):
    text = f"  {text}"
    if indent:
        for _ in range(indent):
            text = f"  {text}"
    if newline:
        print()
    colored_text = colored(text, color)
    print(colored_text, end=end)


def cprint_underlined(text, color="cyan", indent=0, newline=True):
    if newline:
        print()
    cprint(text, indent=indent, color=color)
    terminal_width = get_terminal_width()
    pad = 0
    text = (pad+1)*" " + "-" * (terminal_width - 2*pad-2)
    colored_text = colored(text, color)
    print(colored_text)


def cprint_header(title, color="blue"):
    terminal_width = get_terminal_width()
    title = f"{title} " if len(title) % 2 != 0 else title
    pad = 0
    a = (terminal_width - 2*pad - 2)
    b = int((a - len(title))/2)
    c = pad * ' '
    d = b * ' '
    e = a * '─'
    f = " " if terminal_width % 2 != 0 else ""
    text = "\n"
    text += f"{c}╭{e}╮{c}\n"
    text += f"{c}│{d}{f}{title}{d}│{c}\n"
    text += f"{c}╰{e}╯{c}"
    colored_text = colored(text, color)
    print(colored_text)


def get_terminal_width():
    terminal_size = os.get_terminal_size()
    return terminal_size.columns
