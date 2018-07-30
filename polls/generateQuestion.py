from custommodels import Question, Answer

 import json

 with open('polldb.json') as json_data:
 	dictionary = json.load(json_data)
 q = Question()
 a = Answer()

 for x in dictionary['questions']:
 	q.createQuestion(x)

 for x in dictionary['answers']:
 	a.createAnswer(x)
