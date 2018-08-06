from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class, global_session_class, global_subject_class
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

def createSession(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        global_session_class.create(data)
        return output("True")
    except Exception as e:
        print(e)
        return output("False")

def updateSession(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        ide = data['id']
        global_session_class.update(ide, data)
        return output("True")
    except Exception as e:
        print(e)
        return output("False")

def deleteSession(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        ide = data['id']
        global_session_class.delete(ide)
        return output("True")
    except Exception as e:
        print(e)
        return output("False")

@require_GET
def getAllSessionsByStudentId(request, studentID):
    try:
        cursor = global_session_class.data.find({"students" : studentID})
        cursorList = cursorToList(cursor)
        return JsonResponse(cursorList, safe = False)
    except Exception as e:
        print(e)
        return output('False')

@require_GET
def getAllSessionsByProfessorId(request, professorID):
    try:
        cursor = global_session_class.data.find({"students" : professorID})
        cursorList = cursorToList(cursor)
        return JsonResponse(cursorList, safe = False)
    except Exception as e:
        print(e)
        return output('False')

def getSessionById(request, ide):
    try:
        session_json = global_session_class.data.find_one({"id" : ide})
        session_json["_id"] = ""
        return JsonResponse(session_json, safe = False)
    except Exception as e:
        print(e)
        return output('False')
    
def getAllStudentsBySession(request, ide):
    try:   
        session_json = global_session_class.data.find_one({"id" : ide})
        dict_account = session_json["students"]
        accountList = []
        for x in range(0, len(dict_account), 1):
            account_json = global_account_class.data.find_one({"userID" : dict_account[x]})
            account_json["_id"] = ""
            accountList.append(account_json)
        return JsonResponse(session_json, safe = False)
    except Exception as e:
            print(e)
            return output('False')

def getAllProfessorsBySession(request, ide):
    try:
        session_json = global_session_class.data.find_one({"id" : ide})
        dict_account = session_json["professors"]
        accountList = []
        for x in range(0, len(dict_account), 1):
            account_json = global_account_class.data.find_one({"userID" : dict_account[x]})
            account_json["_id"] = ""
            accountList.append(account_json)
        return JsonResponse(session_json, safe = False)
    except Exception as e:
        print(e)
        return output('False')

def getAllQuestionsBySession(request, ide):
    
    session_json = global_session_class.data.find_one({"id" : ide})
    creatorID = session_json["professors"]
    cursorList = []
    for posCreatorID in range(0, len(creatorID), 1):
        cursor_sessions = global_question_class.data.find({"creatorID" : creatorID[posCreatorID]})
        for x in range(0, cursor_sessions.count(), 1):
            dico = cursor_sessions[x]
            dico["_id"] = ""
            cursorList.append(dico)
    return JsonResponse(cursorList, safe = False)

def addStudentToSession(request):
	try:
		data = json.loads(request.body.decode('utf-8'))
	`	session_json = global_session_class.data.find_one({'id' : data['sessionID']})
		list_student = session_json['students']
		list_student.append(data['studentID'])
		global_session_class.update(data['sessionID'], {'students' : list_student})
		return output('True')
	except Exception as e:
		print(e)
		return output('False')

def addProfToSession(request):
	try:
		data = json.loads(request.body.decode('utf-8'))
		session_json = global_session_class.data.find_one({'id' : data['sessionID']})
		list_prof = session_json['professors']
		list_prof.append(data['professorID'])
		global_session_class.update(data['sessionID'], {'professors' : list_prof})
		return output('True')
	except Exception as e:
		print(e)
		return output('False')
