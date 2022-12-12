from django.urls import path
from .views import *

urlpatterns = [
	path('registration', registration),
	path('ajax_check_username', ajax_check_username),
	path('ajax_check_email', ajax_check_email),
	path('confirm', confirm),
	path('entry', entry),
	path('out', out),
	path('profile', profile),
	path('reset', reset),
]