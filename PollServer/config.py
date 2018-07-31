from pymongo import MongoClient

#CONFIF
CLIENT = MongoClient('127.0.0.1', 27017)
PORT_NAME = 8000
HOST_NAME = '0.0.0.0'
DATABASE = CLIENT.db


#GLOBALIZE
def set_global():
	global PORT_NAME, HOST_NAME, DATABASE
set_global()
