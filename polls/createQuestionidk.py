import json
from custommodels import Question
Question().data.drop()
f = open("db.json", "r")
j = json.load(f)
Question().data.insert_many(j)

