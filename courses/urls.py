from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('index', index),
	path('<slug:slug>/', views.CourseDetailView.as_view()),
	path('studentsform', students_app)
]