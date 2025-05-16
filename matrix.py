import os
import random
import shutil
import sys
import time
from colorama import init, Fore, Style, Cursor

init()
os.system('color 0a')

# Option 1: auto detect terminal size
# cols, rows = shutil.get_terminal_size()

# Option 2: manual override for more horizontal characters
cols = 200  # Adjust this to your window width
rows = 80   # Adjust to your window height

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*()"

drops = [random.randint(-rows, 0) for _ in range(cols)]

try:
    while True:
        for i in range(cols):
            tail_pos = drops[i] - 4
            if 0 <= tail_pos < rows:
                print(Cursor.POS(i + 1, tail_pos + 1) + ' ', end='')

            for t in range(3, 0, -1):
                trail_pos = drops[i] - t
                if 0 <= trail_pos < rows:
                    print(Cursor.POS(i + 1, trail_pos + 1) + Fore.GREEN + random.choice(chars) + Style.RESET_ALL, end='')

            head_pos = drops[i]
            if 0 <= head_pos < rows:
                print(Cursor.POS(i + 1, head_pos + 1) + Fore.WHITE + random.choice(chars) + Style.RESET_ALL, end='')

            drops[i] += 1
            if drops[i] > rows + random.randint(0, 15):
                drops[i] = random.randint(-20, 0)

        sys.stdout.flush()
        time.sleep(0.05)

except KeyboardInterrupt:
    print(Style.RESET_ALL)
    os.system('cls')
    os.system('color 07')
    sys.exit()
