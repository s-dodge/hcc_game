from rich.table import Table
from rich.console import Console
import sys
import time
import subprocess
import os
import msvcrt
import random
import unicodedata

ZALGO_UP = [chr(c) for c in range (0x0300, 0x036F)]
ZALGO_DOWN = [chr(c) for c in range(0x0316, 0x0333)]

def zalgo_corrupt(text,intensity=1):
    result = []
    for char in text:
        result.append(char)
        if char.isalpha():
            for _ in range(random.randint(0, intensity * 2)):
                result.append(random.choice(ZALGO_UP))
            for _ in range(random.randint(0, intensity)):
                result.append(random.choice(ZALGO_DOWN))
    return ''.join(result)

# --- typewriter function for better text presentation ---
def typewrite(text: str, char_delay: float = 0.03, line_delay: float = 0.4) -> str:
    # Drain buffered keypresses so a prior input() doesn't trigger a skip
    while msvcrt.kbhit():
        msvcrt.getch()

    for i, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in (b' ', b'\r'):
                while msvcrt.kbhit():  # drain any remaining buffer
                    msvcrt.getch()
                sys.stdout.write(text[i + 1:])
                sys.stdout.flush()
                break
        if char == "\n":  # increase delay for new lines for better flow
            time.sleep(line_delay)
        else:
            time.sleep(0.001 if unicodedata.combining(char) else char_delay)

    print()

def pause():
    input("")
    sys.stdout.write("\033[A\033[K")
    sys.stdout.flush()

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def set_window():
    try:
        sys.stdout.write('\033[8;45;120t')
        sys.stdout.flush()
    except Exception:
        pass

def display_inventory(inventory):
    console = Console()

    table = Table(title="Inventory", show_lines=True)

    table.add_column("Item", justify="center", max_width=60)
    table.add_column("Description", justify="center",max_width=60)

    for item in inventory:
        table.add_row(item.name, item.description)
    
    console.print(table)

def show_title_block():
    print(r"""

                +=========================================================================================+
                |                                     WELCOME TO THE                                      |
                |                                                                                         |
                |                                                                                         |
                |            ██░ ██  ▄████▄   ▄████▄      ██░ ██ ▓█████  ██▓     ██▓███                   |
                |           ▓██░ ██▒▒██▀ ▀█  ▒██▀ ▀█     ▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒                 |
                |           ▒██▀▀██░▒▓█    ▄ ▒▓█    ▄    ▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒                 |
                |           ░▓█ ░██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒                 |
                |           ░▓█▒░██▓▒ ▓███▀ ░▒ ▓███▀ ░   ░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░                 |
                |            ▒ ░░▒░▒░ ░▒ ▒  ░░ ░▒ ▒  ░    ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░                 |
                |            ▒ ░▒░ ░  ░  ▒     ░  ▒       ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░                      |
                |            ░  ░░ ░░        ░            ░  ░░ ░   ░     ░ ░   ░░                        |
                |            ░  ░  ░░ ░      ░ ░          ░  ░  ░   ░  ░    ░  ░                          |
                |                   ░        ░                                                            |
                |                             ▓█████▄ ▓█████   ██████  ██ ▄█▀                             |
                |                             ▒██▀ ██▌▓█   ▀ ▒██    ▒  ██▄█▒                              |
                |                             ░██   █▌▒███   ░ ▓██▄   ▓███▄░                              |
                |                             ░▓█▄   ▌▒▓█  ▄   ▒   ██▒▓██ █▄                              |
                |                             ░▒████▓ ░▒████▒▒██████▒▒▒██▒ █▄                             |
                |                              ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒                             |
                |                              ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░░ ░▒ ▒░                             |
                |                              ░ ░  ░    ░   ░  ░  ░  ░ ░░ ░                              |
                |                                ░       ░  ░      ░  ░  ░                                |
                |                              ░                                                          |
                |      ▄▄▄      ▓█████▄  ██▒   █▓▓█████  ███▄    █ ▄▄▄█████▓ █    ██  ██▀███  ▓█████      |
                |     ▒████▄    ▒██▀ ██▌▓██░   █▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀      |
                |     ▒██  ▀█▄  ░██   █▌ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒███        |
                |     ░██▄▄▄▄██ ░▓█▄   ▌  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄      |
                |      ▓█   ▓██▒░▒████▓    ▒▀█░  ░▒████▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▒████▒     |
                |      ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░     |
                |       ▒   ▒▒ ░ ░ ▒  ▒    ░ ░░   ░ ░  ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░     |
                |       ░   ▒    ░ ░  ░      ░░     ░      ░   ░ ░   ░       ░░░ ░ ░   ░░   ░    ░        |
                |           ░  ░   ░          ░     ░  ░         ░             ░        ░        ░  ░     |
                |                ░           ░                                                            |
                |                                                                                         |
                |                                     Press Enter to begin                                |
                |                                         or Q to quit                                    |
                +=========================================================================================+

""")

if __name__ == "__main__":
    typewrite("there's nothing here")


