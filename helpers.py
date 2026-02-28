import sys
import time
import subprocess
import os

# --- typewriter function for better text presentation ---
def typewrite(text: str, char_delay: float = 0.03, line_delay: float = 0.4) -> str:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == "\n":  # increase delay for new lines for better flow
            time.sleep(line_delay)
        else:
            time.sleep(char_delay)
    print()

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


if __name__ == "__main__":
    typewrite("there's nothing here")

