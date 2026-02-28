import sys
import time
import subprocess
import os

def typewrite(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


if __name__ == "__main__":
    typewrite("there's nothing here")

