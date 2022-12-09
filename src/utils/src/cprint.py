import os

from termcolor import colored


def cprint(text, color="cyan", indent=0, newline=False, end="\n"):
    text = f"  {text}"
    if indent:
        for _ in range(indent):
            text = f"  {text}"
    if newline:
        text = f"\n{text}"
    colored_text = colored(text, color)
    print(colored_text, end=end)


def cprint_header(title, color="blue"):
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns
    title = f"{title} " if len(title) % 2 != 0 else title
    pad = 3
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
