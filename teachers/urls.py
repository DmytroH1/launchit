from django.urls import path
from .views import *

urlpatterns = [
	path('index', index),
	path('ajax_del_teacher', ajax_del_teacher)
]