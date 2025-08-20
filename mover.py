from pyautogui import scroll
from time import sleep

def main():
    direction = 1  # 1 for up, -1 for down
    while True:
        scroll(5 * direction)  # Scroll slightly
        direction *= -1        # Alternate direction
        sleep(10)              # Wait 10 seconds

main()
