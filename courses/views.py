from django.shortcuts import render, redirect
from .models import Category, Course
from django.views.generic.base import View
from .form import AppForm


def index(request):
	all_courses = Course.objects.all()
	return render(request, 'courses/index.html', {
		'page_title': 'Каталог курсів',
		'all_courses': all_courses,
		'all_categories': Category.objects.all()
	})


class CourseDetailView(View):
	def get(self, request, slug):
		c = Course.objects.get(url=slug)
		return render(request, 'courses/course.html', {
			'course': c,
			'page_title': 'Опис курсу'
		})


def students_app(request):
	if request.method == 'GET':
		return render(request, 'courses/studentsform.html', {
			'page_title': 'Форма заявки'
	})
	elif request.method == 'POST':
		form = AppForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
