from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
from .setup import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib
from pymongo import cursor
import traceback

# Create your views here.
def output(error_message = "False"):
	return JsonResponse({'update' : error_message})

@api_view(['POST'])
@csrf_exempt
def submitAnswer(request):
	try:
		data_json = json.loads(request.body.decode("utf-8"))

		global_answer_class.create(data_json)
		return JsonResponse({'update' : True})
	except Exception as e:
		print(e)
		return JsonResponse({'update' : False})

#@require_GET
def getAnswer(request, ide): # ide is questionID
	try:
		answer_json = global_answer_class.data.find({'questionID' : ide}) # get the users answers.
		question_json = global_question_class.getDictById(ide) # get the question of the answer
		if question_json['type'] == 1:
			answers = range(question_json['answers']['min'], question_json['answers']['max'], question_json['answers']['step'])
		else:
			answers = question_json['answers'] # get answer choices
		data = {}
		data["questionID"] = question_json['id']
		data["text"] = question_json['text']
		data["images"] = question_json['images']
		data["video"] = question_json['video']
		list_answers = [] # data output
		print(answers)
		for j in answers:
			cursor = global_answer_class.data.find({'answers' : j})
			print(cursor.count())
			user = []
			for i in cursor:
				user.append(i['userID'])
			list_answers.append({'value' : j, 'users' : user})
		data["answers"] = list_answers
		return JsonResponse(data, safe = False) # return data
	except Exception as e:
		traceback.print_exc()
		return output('False')

@require_GET
def getAllAnswersByQuestionId(request, questionID):
	try:
		cursor = global_answer_class.data.find({"questionID" : questionID})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dico["_id"] = ""
			cursorList.append(dico)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

