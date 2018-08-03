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
