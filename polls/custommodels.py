from pymongo import MongoClient
from PollServer.config import *
import json

class Question:
	def __init__(self):
		self.data = database.question
		if self.data.find_one({'count' : 'count'}) == None:
			self.data.insert_one({'count' : 'count', 'length' : 0})
	def createQuestion(self, question_json):
		"""createQuestion(question_json)"""
		count = self.data.find_one({'count' : 'count'})
		count = count['length']

		ide = 'q' + str(count + 1)
		question_json['id'] = ide

		self.data.insert_one(question_json)
		self.data.update_one({'count' : 'count'}, {'$inc' : {'length' : 1}})

	def updateQuestion(self, ide , what_to_update):
		"""updateQuestion(id , what_to_update)

		what_to_update -> dict.   for example : {'type' : 0, 'text : 'idk'}
		"""
		self.data.update_one({'id' : ide}, {'$set' : what_to_update})

	def getQuestionById(self, ide):
		"""getQuestionById(id)"""
		q = self.data.find_one({'id' : ide})
		if q != None:
			q['_id'] = ''
			return q
		return None

	def deleteQuestion(self, *args):
		"""Still in Beta version
		deleteQuestion(id)

		Argument example: {'id' : 'q1'} or {'id' : 'q1'}, 'id' : 'q2'}"""
		for x in args:
			self.data.remove(x)

class Answer:
	def __init__(self):
		self.data = database.answer
		if self.data.find_one({'count' : 'count'}) == None:
			self.data.insert_one({'count' : 'count', 'length' : 0})
			
	def createAnswer(self, answer_json):
		"""createAnswer()"""
		count = self.data.find_one({'count' : 'count'})
		count = count['length']
		
		ide = 'a' + str(count + 1)
		answer_json['id'] = ide
		
		self.data.insert_one(answer_json)
		self.data.update_one({'count' : 'count'}, {'$inc' : {'length' : 1}})
		
	def updateAnswer(self, ide, to_update):
		"""updateAnswer(id , to_update, new)

		"""
		self.data.update_one({'id' : ide}, {'$set' : to_update})
	
	def getAnswerById(self, ide):
		"""getAnswerById(id)"""
		a = self.data.find_one({"id" : ide})
		if a != None:
			a['_id'] = ''
			return a
		else:
			return None

	def getAnswersByQuestionId(self, questionID):
		cursor = self.data.find({'questionID' : questionID})
		answer_list = []
		if cursor == None:
			return None
		for x in cursor:
			x['_id'] = ''
			answer_list.append(x)
		return answer_list
class Account:
	def __init__(self):
		self.data = database.user_account
		if self.data.find_one({'count' : 'count'}) == None:
			self.data.insert_one({'count' : 'count', 'length' : 0})
	
	def createAccount(self, account_json):
		"""createAccount(account_json)"""
		count = self.data.find_one({'count' : 'count'})
		count = count['length']

		ide = 'u' + str(count + 1)
		account_json['id'] = ide

		self.data.insert_one(account_json)
		self.data.update_one({'count' : 'count'}, {'$inc' : {'length' : 1}})
		
	def updateAccount(self, ide, to_update):
		"""updateAccount(id, to_update)

		to_update -> dict.   for example : {'type' : 0, 'text : 'idk'}
		"""
		self.data.update_one({'id' : ide}, {'$set' : to_update})
		
	def getAccountById(self, ide):
		"""getAccountById(id)"""
		u = self.data.find_one({"id" : ide})
		if u != None:
			u['_id'] = ''
			return u
		else:
			return None	
		
	def userLogin(self, login_json):
		user = self.data.find_one({"username" : login_json["username"], "password" : login_json["password"]})
		if user != None:
			return True
		else:
			return False
