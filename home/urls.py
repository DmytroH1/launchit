from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', index),
	path('about', about),
	path('contacts', contacts),
	path('news', news),
	path('<slug:slug>/', views.NewsDetailView.as_view())
]