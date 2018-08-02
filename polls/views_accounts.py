from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
from .setup import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib
from pymongo import cursor

# Create your views here.
def output(error_message = "False"):
	return JsonResponse({'update' : error_message})

@api_view(['POST'])
@csrf_exempt
def checkLogin(request):
	try:
		login_json = json.loads(request.body)
		hash = hashlib.md5(login_json["password"].encode())
		hash = hash.hexdigest()
		login_json["password"] = hash
		account_login = global_account_class.userLogin(login_json)
		if account_login == True:
			return HttpResponse("True")
		else:
			return HttpResponse("False")
	except Exception as e:
		print(e)
		return output('False')

@api_view(['POST'])
@csrf_exempt
def newAccount(request):
	try:
		form_json = json.loads(request.body) # form_json = {"username" : "asdf", "password" : "af"}
		hash = hashlib.md5(form_json["password"].encode())
		hash = hash.hexdigest()
		form_json["password"] = hash
		global_account_class.create(form_json)
	except Exception as e:
		print(e)
		return output('False')

