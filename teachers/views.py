from django.shortcuts import render
from .models import Teachers
from django.http import JsonResponse


def index(request):
	all_teachers = Teachers.objects.all()
	return render(request, 'teachers/index.html', {
		'page_title': 'Наші викладачі',
		'all_teachers': all_teachers
	})


def ajax_del_teacher(request):
	del_teacher_id = request.GET['del_teacher_id']
	del_teacher = Teachers.objects.get(id=del_teacher_id)
	del_teacher.delete()
	return JsonResponse({
		'report': f'Вчитель із ID: {del_teacher_id} був видалений з таблиці!'
	})