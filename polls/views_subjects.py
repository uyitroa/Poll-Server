from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class, global_session_class, global_subject_class
from .setup import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib

# Create your views here.
def output(error_message = "False"):
    return JsonResponse({'update' : error_message})

def getAllSubjectsByStudentId(request, studentID):
    try:
        cursor = global_subject_class.data.find({"students" : studentID})
        cursorList = []
        for x in range(0, cursor.count(), 1):
            dico = cursor[x]
            dico["_id"] = ""
            cursorList.append(dico)
        return JsonResponse(cursorList, safe = False)
    except Exception as e:
        print(e)
        return output('False')
    
def getAllSubjectsByProfessorId(request, professorID):
    try:
        cursor = global_subject_class.data.find({"students" : professorID})
        cursorList = []
        for x in range(0, cursor.count(), 1):
            dico = cursor[x]
            dico["_id"] = ""
            cursorList.append(dico)
        return JsonResponse(cursorList, safe = False)
    except Exception as e:
        print(e)
        return output('False')

def getSubjectById(request, ide):
    try:
        subject_json = global_subject_class.data.find_one({"id" : ide})
        subject_json["_id"] = ""
        return JsonResponse(subject_json, safe = False)
    except Exception as e:
        print(e)
        return output('False')
    
def submitSubject(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        global_subject_class.create(data)
        return output("True")
    except Exception as e:
        print(e)
        return output("False")
    
def updateSubject(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        ide = data['id']
        global_subject_class.update(ide, data)
        return output("True")
    except Exception as e:
        print(e)
        return output("False")

def deleteSubject(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        ide = data['id']
        global_subject_class.delete(ide)
    except Exception as e:
        print(e)
        return output("False")

def getAllStudentsBySubject(request, ide):
    try:
        subject_json = global_session_class.data.find_one({"id" : ide})
        dict_account = subject_json["students"]
        accountList = []
        for x in range(0, len(dict_account), 1):
            account_json = global_account_class.data.find_one({"userID" : dict_account[x]})
            account_json["_id"] = ""
            accountList.append(account_json)
        return JsonResponse(subject_json, safe = False)
    except Exception as e:
            print(e)
            return output('False')
    
def getAllProfessorsBySubject(request, ide):
    try:
        subject_json = global_session_class.data.find_one({"id" : ide})
        dict_account = subject_json["professors"]
        accountList = []
        for x in range(0, len(dict_account), 1):
            account_json = global_account_class.data.find_one({"userID" : dict_account[x]})
            account_json["_id"] = ""
            accountList.append(account_json)
        return JsonResponse(subject_json, safe = False)
    except Exception as e:
            print(e)
            return output('False')

def getAllSubjects(request, ide):
    try:
        cursor = global_subject_class.data.find({"id" : ide})
        subjectList = []
        for x in range(0, cursor.count(), 1):
            dico = cursor[x]
            dico["_id"] = ""
            subjectList.append(dico)
        return JsonResponse(subjectList, safe = False)
    except Exception as e:
            print(e)
            return output('False')

def addProfToSubject(request):
	try:
		data = json.loads(request.body.decode("utf-8"))
		subject_json = global_subject_class.find_one({"id" : data["subjectID"]})
		list_prof = subject_json['professors']
		list_prof.append(data["professorID"])
		global_subject_class.update(data['sessionID'], {'professors' : list_prof})
		return output('True')
	except Exception as e:
		print(e)
		return output("False")

def addStudentToSubject(request):
	try:
		data = json.loads(request.body.decode("utf-8"))
		subject_json = global_subject_class.find_one({'id' : data['subjectID']})
		list_student = subject_json['students']
		list_student.append(data['studentID'])
		global_subject_class.update(data['subjectID'], {'students' : list_student})
		return output('True')
	except Exception as e:
		print(e)
		return output('False')
