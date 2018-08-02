#python3
import sys
sys.path.append("../")
from pymongo import MongoClient
from PollServer.config import *
import json

client = MongoClient('localhost', 27017)
DATABASE = client.get_database(DATABASE)

class Model:
	def __init__(self, datapath, id_format):
		self.data = datapath
		self.id_format = id_format
		if self.data.find_one({'count' : 'count'}) == None:
			self.data.insert_one({'count' : 'count', 'length' : self.data.find().count()})

	def create(self, json_data):
		"""create(data_format_json)"""
		count = self.data.find_one({'count' : 'count'})
		count = count['length']

		ide = self.id_format + str(count + 1)
		json_data['id'] = ide

		self.data.insert_one(json_data)
		self.data.update_one({'count' : 'count'}, {'$inc' : {'length' : 1}})

	def update(self, ide, what_to_update):
		"""update(id, what_to_update)
		what_to_update = dict of stuff to update"""
		self.data.update_one({'id' : ide}, {'$set' : what_to_update})

	def getDictById(self, ide):
		"""getDictById(ide)"""
		data = self.data.find_one({'id' : ide})
		if data != None:
			data['_id'] = ''
		return data

	def delete(self, *args):
		"""delete(*id) #multiple args
		ex: {'id' : 'q1'} or {'id' : 'q1'}, {'id' : 'q2'}"""
		for x in args:
			self.data.remove(x)

class Question(Model):
	def __init__(self):
		Model.__init__(self, DATABASE.question, 'q')

class Answer(Model):
	def __init__(self):
		Model.__init__(self, DATABASE.answer, 'a')
			
class Account(Model):
	def __init__(self):
		Model.__init__(self, DATABASE.account, 'acc')
	
	def userLogin(self, login_json):
		user = self.data.find_one({"username" : login_json["username"], "password" : login_json["password"]})
		if user != None:
			return True
		else:
			return False

class Session(Model):
	def __init__(self):
		Model.__init__(self, DATABASE.session, 's')
