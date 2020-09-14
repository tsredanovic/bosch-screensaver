from time import sleep
from datetime import datetime

def do_something(text):
    with open("/home/toni/Projects/bosch-screensaver/systemd_test/test.txt", "a") as myfile:
        myfile.write('{} - {}\n'.format(datetime.now(), text))


do_something('Started.')
while True:
    sleep(5)
    do_something('Did something.')
