
import os
from subprocess import call
from time import sleep


BASE = os.path.dirname(__file__)
MANAGE_BASE = os.path.join(BASE, 'manage.py')

while True:
    call(['python', MANAGE_BASE, 'ttl'])
    sleep(5)
