from django.shortcuts import render


def index(request):
	return render(request, 'courses/index.html', {
		'page_title': 'Каталог курсів'
	})