from PollServer.config import *
import os

name = host_name + ":" + str(port_name)
os.system("python3 manage.py runserver " + name)
