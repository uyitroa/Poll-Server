from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class, global_session_class, global_subject_class
from .setup import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import hashlib

# Create your views here.
def output(error_message = "False"):
	return JsonResponse({'update' : error_message})

@require_GET
def getQuestion(request, ide):
	try:
		question_json = global_question_class.getDictById(ide)

		if question_json == None:
			return output('False')
		response = JsonResponse(question_json)
		return response
	except Exception as e:
		print(e)
		return output('False')

def submitQuestion(request):
	try:
		data = json.loads(request.body.decode("utf-8"))
		global_question_class.create(data)
		return output("True")
	except Exception as e:
		print(e)
		return output("False")

def updateQuestion(request):
	try:
		data = json.loads(request.body.decode("utf-8"))
		ide = data['id']
		global_question_class.update(ide, data)
		return output("True")
	except Exception as e:
		print(e)
		return output("False")

def deleteQuestion(request):
	try:
		data = json.loads(request.body.decode("utf-8"))
		ide = data['id']
		global_question_class.delete(ide)
	except Exception as e:
		print(e)
		return output("False")

@require_GET
def getCreatorQuestionByStatus(request, creatorID, status):
	try:
		cursor = global_question_class.data.find({'creatorID' : creatorID, 'status' : status})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dico['_id'] = ''
			cursorList.append(dico)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

@require_GET	
def getQuestionsByCreatorId(request, creatorID):
	try:
		cursor = global_question_class.data.find({"creatorID" : creatorID})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dico['_id'] = ''
			cursorList.append(dico)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

@require_GET
def getQuestionsByUserId(request, userID):
	try:
		cursor = global_answer_class.data.find({"userID" : userID})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dicte = global_question_class.data.find_one({"id" : dico["questionID"]})
			dicte['_id'] = ''
			cursorList.append(dicte)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

@require_GET
def getAllUsersByQuestionText(request, text):
	try:
		dict_questions = global_question_class.data.find_one({"text" : text})
		dict_id = dict_questions["id"]
		questionID = dict_id
		cursorList = []
		cursor_answers = global_answer_class.data.find({"questionID" : questionID})
		for x in range(0, cursor_answers.count(), 1):
			dico = cursor_answers[x]
			cursorList.append(dico["userID"])
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

