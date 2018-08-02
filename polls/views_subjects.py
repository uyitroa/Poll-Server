from django.shortcuts import render
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
        print(cursor.count())
        return JsonResponse(cursorList, safe = False)
    except Exception as e:
        print(e)
        return output('False') 
    