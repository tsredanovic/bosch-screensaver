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
    started_at = datetime.now()
    while True:
        if not screensaver_is_on():
            return 'EXTERNAL', (datetime.now() - started_at).total_seconds()
        seconds_on = (datetime.now() - started_at).total_seconds()
        if seconds_on > N:
            stop_screensaver()
            return 'TIMEOUT', (datetime.now() - started_at).total_seconds()


def screensaver_is_on():
    p = subprocess.run(['xscreensaver-command', '-time'], stdout=subprocess.PIPE)
    words = p.stdout.decode().split()
    return 'blanked' in words

# Check screensaver every second
# If the screensaver is off, do nothing
# If the screensaver is on, turn it off after N second

while True:
    if screensaver_is_on():
        print('{} - Screensaver ON'.format(datetime.now()))
        stopped_by, seconds_on = stop_screensaver_after_n()
        print('{} - Screensaver OFF by {}, was on for {} seconds'.format(datetime.now(), stopped_by, seconds_on))


started_at = datetime.now()
sleep(75)
current_time = datetime.now()
import pdb
pdb.set_trace()