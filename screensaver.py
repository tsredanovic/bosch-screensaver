import logging
import subprocess
from time import sleep
from datetime import datetime

import pyautogui
import cv2

LOG_FILE_PATH = '/home/toni/Projects/bosch-screensaver/screensaver.log' # Log file
OPENCV_FILE_PATH = '/home/toni/Projects/bosch-screensaver/opencv/haarcascade_frontalface_default.xml' # Model for recognizing faces
N = 30  # Number of seconds the screensaver plays

def stop_screensaver():
    if pyautogui.position() != (1, 1):
        pyautogui.moveTo(1, 1)
    else:
        pyautogui.moveTo(20, 20)


def stop_screensaver_after_n_or_face():
    started_at = datetime.now()
    cap = cv2.VideoCapture(0)
    while True:
        # Check if the screensaver is on
        if not screensaver_is_on():
            cap.release()
            return 'EXTERNAL', (datetime.now() - started_at).total_seconds()
        
        # Check if time out
        seconds_on = (datetime.now() - started_at).total_seconds()
        if seconds_on > N:
            stop_screensaver()
            cap.release()
            return 'TIMEOUT', (datetime.now() - started_at).total_seconds()
        
        # Check for face
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces):
            stop_screensaver()
            cap.release()
            return 'FACE', (datetime.now() - started_at).total_seconds()


def screensaver_is_on():
    p = subprocess.run(['xscreensaver-command', '-time'], stdout=subprocess.PIPE)
    words = p.stdout.decode().split()
    return 'blanked' in words

# Init CascadeClassifier
face_cascade = cv2.CascadeClassifier(OPENCV_FILE_PATH)

# Init logging
logging.basicConfig(filename=LOG_FILE_PATH,level=logging.DEBUG)

# Check screensaver every second
# If the screensaver is off, do nothing
# If the screensaver is on, turn it off after N seconds or after cam sees a face
logging.info('{} - Started'.format(datetime.now()))
while True:
    if screensaver_is_on():
        logging.info('{} - Screensaver ON'.format(datetime.now()))
        stopped_by, seconds_on = stop_screensaver_after_n_or_face()
        logging.info('{} - Screensaver OFF by {}, was on for {} seconds'.format(datetime.now(), stopped_by, seconds_on))
