from pymongo import MongoClient

class Question:
	def __init__(self):
		self.client = MongoClient('127.0.0.1', 27017)
		self.data = self.client.db.question
		if self.data.find_one({'count' : 'count'}) == None:
			self.data.insert_one({'count' : 'count', 'length' : 0})
	def createQuestion(self, question_json):

		"""createQuesiton(question_json)"""
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

		stuff = self.data.find_one({'id' : ide})

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
		self.client = MongoClient('127.0.0.1', 27017)
		self.data = self.client.db.answer
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
		stuff = self.data.find_one({'id' : ide})

		self.data.update_one({'id' : ide}, {'$set' : to_update})
	
	def getAnswerById(self, ide):
		"""getAnswerById(id)"""
		a = self.data.find_one({"id" : ide})
		if a != None:
			a['_id'] = ''
			return a
		else:
			return None
