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
from polls import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('questions/<str:ide>/', views.getQuestion, name = 'getQuestion'),
	path('questions/<str:ide>/answers/', views.getAnswer, name = 'getAnswer'),
	path('answers/', views.submitAnswer, name = 'submitAnswer'),
	path('questions/',  views.submitQuestion, name = 'submitQuestion'),
	path('login/', views.checkLogin, name = 'checkLogin'),
	path('questions/<str:creatorID>/<int:status>/', views.getCreatorQuestionByStatus, name = 'getCreatorQuestionByStatus'),
    path('questions/creatorID/<str:creatorID>/', views.getQuestionsByCreatorId, name = 'getQuestionsByCreatorId'),
    path('questions/userID/<str:userID>/', views.getQuestionsByUserId, name = 'getQuestionsByUserId'),
]
