import subprocess
from time import sleep
from datetime import datetime

import pyautogui

N = 10  # Number of seconds the screensaver plays

def stop_screensaver():
    if pyautogui.position() != (1, 1):
        pyautogui.moveTo(1, 1)
    else:
        pyautogui.moveTo(20, 20)


def stop_screensaver_after_n():
    sec_passed = 0
    while sec_passed < N:
        sleep(1)
        if not screensaver_is_on():
            return False
        sec_passed += 1
    stop_screensaver()
    return True


def screensaver_is_on():
    p = subprocess.run(['xscreensaver-command', '-time'], stdout=subprocess.PIPE)
    words = p.stdout.decode().split()
    return 'blanked' in words

# Check screensaver every second
# If the screensaver is off, do nothing
# If the screensaver is on, turn it off after N second
while True:
    sleep(1)
    if screensaver_is_on():
        print('{} - Screensaver turned ON'.format(datetime.now()))
        stopped_by_me = stop_screensaver_after_n()
        print('{} - Screensaver turned OFF by {}'.format(datetime.now(), 'ME' if stopped_by_me else 'SOMETHING ELSE'))
