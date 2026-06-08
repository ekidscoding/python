from rich.console import Console
from rich.theme import Theme

DARK_MODE = True

light_theme = {
    "code": "green",
    "info": "blue1",
    "header": "blue1 bold",
    "warn": "dark_orange3",
    "error": "dark_red",
    "tip": "dark_violet",
    "repr.number": "orange3",
    "repr.str": "chartreuse4",
    "repr.call": "medium_orchid1"
}

dark_theme = {
    "code": "sea_green1",
    "info": "deep_sky_blue1",
    "header": "deep_sky_blue1 bold",
    "warn": "orange1",
    "error": "bright_red",
    "tip": "violet",
    "repr.number": "bright_yellow",
    "repr.str": "green1",
    "repr.call": "orchid1"
}

selected_theme = dark_theme if DARK_MODE else light_theme

console = Console(theme=Theme(selected_theme))

def section(length=30):
    console.print("〰"*length)

def line():
    console.line()

def print_header(*args):
    section()
    console.print("🔘", *args, style="header")
    line()

def print_code(*args):
    console.print(*args, style="code")
    line()

def print_info(*args):
    console.print(*args, style="info")
    line()

def print_warn(*args):
    console.print(*args, style="warn")
    line()

def print_error(*args):
    console.print(*args, style="error")
    line()

def print_tip(*args):
    console.print("\tTIP:\n\t", *args, style="tip")
    line()