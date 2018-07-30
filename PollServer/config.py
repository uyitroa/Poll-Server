from pymongo import MongoClient

#CONFIG
client = MongoClient('127.0.0.1', 27017)
port_name = 8000
host_name = '0.0.0.0'
database = client.db


#GLOBALIZE
def set_global():
	global port_name, host_name, database
set_global()
