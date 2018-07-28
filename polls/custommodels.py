from pymongo import MongoClient

class Question:
	def __init__(self):
		self.client = MongoClient('127.0.0.1', 27017)
		self.data = self.client.db.question

	def createQuestion(self, question_json):
		"""createQuestion(type, text, answers, images, video)"""
		count = self.data.estimated_document_count() + 1
		ide = 'q' + str(count)
		self.data.insert_one(question_json)

	def updateQuestion(self, ide , what_to_update):
		"""updateQuestion(id , what_to_update, new)

		what_to_update -> string.   for example : 'id', 'type', 'text'
		"""

		stuff = self.data.find_one({'id' : ide})

		self.data.update_one({'id' : ide}, {'$set' : what_to_update})

	def getQuestionById(self, ide):
		"""getQuestionById(id)"""
		q = self.data.find_one({'id' : ide})
		if q != None:
			return q['text']
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
		
	def createAnswer(self, answer_json):
		"""createAnswer()"""
		count = self.data.estimated_document_count() + 1
		ide = "a" + str(count)
		self.data.insert_one(answer_json)
		
	def updateAnswer(self, ide, to_update):
		"""updateAnswer(id , to_update, new)

		to_update -> string.   for example : 'id', 'type', 'text'
		"""
		stuff = self.data.find_one({'id' : ide})

		self.data.update_one({'id' : ide}, {'$set' : to_update})
	
	def getAnswerById(self, ide):
		"""getAnswerById(id)"""
		a = self.data.find_one({"id" : ide})
		if a != None:
			return a["answer"]
		else:
			return None