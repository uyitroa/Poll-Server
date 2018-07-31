from PollServer.config import *
import os

name = HOST_NAME + ":" + str(PORT_NAME)
os.system("python3 manage.py runserver " + name)
