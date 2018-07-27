from pymongo import MongoClient

class Question:
	def __init__(self):
		self.client = MongoClient('127.0.0.1', 27017)
		self.data = self.client.db.question

	def createQuestion(self, ide, question_type, question_text, answers, images = [], video = None):
		"""createQuesiton(id, type, text, answers, images, video)"""
		stuff = {
			'id' : ide,
			'type' : question_type,
			'text' : question_text,
			'video' : video,
			'images' : images,
			'answers' : answers
			}

		self.data.insert_one(stuff)

	def updateQuestion(self, ide ,what_to_update, new):
		"""updateQuestion(id , what_to_update, new)

		what_to_update -> string.   for example : 'id', 'type', 'text'
		"""

		stuff = self.data.find_one({'id' : ide})

		self.data.update_one({'id' : ide}, {'$set' :  {
				what_to_update : new
			}
		})
