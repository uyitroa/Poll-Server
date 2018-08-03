"""PollServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from polls import views_questions, views_answers, views_accounts, views_sessions, views_subjects
from polls import views
urlpatterns = [
	#path('admin/', admin.site.urls),
	path('questions/<str:ide>/', views.getQuestion, name = 'getQuestion'),
	path('questions/<str:ide>/answers/', views.getAnswer, name = 'getAnswer'),

	path('answers/submit/', views.submitAnswer, name = 'submitAnswer'),

	path('questions/submit/',  views.submitQuestion, name = 'submitQuestion'),
	path('questions/update/', views.updateQuestion, name = 'updateQuestion'),
	path('questions/delete/', views.deleteQuestion, name = 'deleteQuestion'),

	path('questions/<str:creatorID>/<int:status>/', views.getCreatorQuestionByStatus, name = 'getCreatorQuestionByStatus'),
	path('questions/creator/<str:creatorID>/', views.getQuestionsByCreatorId, name = 'getQuestionsByCreatorId'),
	path('questions/user/<str:userID>/', views.getQuestionsByUserId, name = 'getQuestionsByUserId'),
	path('questions/allanswers/<str:questionID>/', views.getAllAnswersByQuestionId, name = 'getAllAnswersByQuestionId'),
	
	path('subjects/allstudents/<str:studentID>/', views.getAllSubjectsByStudentId, name = 'getAllSubjectsByStudentId'),
	path('subjects/<str:ide>/', views.getSubjectById, name = 'getSubjectById'),
	path('subjects/submit/',  views.submitSubject, name = 'submitSubject'),
	path('subjects/update/', views.updateSubject, name = 'updateSubject'),
	path('subjects/delete/', views.deleteSubject, name = 'deleteSubject'),
	
	path('login/', views.checkLogin, name = 'checkLogin'),

	path('sessions/submit/', views.createSession, name = 'createSession'),
	path('sessions/update/', views.updateSession, name = 'updateSession'),
	path('sessions/delete/', views.deleteSession, name = 'deleteSession'),
	path('sessions/<str:ide>/', views.getSessionById, name = 'getSessionById'),
	path('sessions/allstudents/<str:studentID>/', views.getAllSessionsByStudentId, name = 'getAllSessionsByStudentId'),
	
	path('accounts/<str:typeID>/', views.getUserByTypeId, name = 'getUserByTypeId'),
	
]
