from django.shortcuts import render
from .form import FeedbackForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.base import View
from .models import News


def index(request):
	return render(request, 'home/index.html', {
		'page_title': 'Головна'
	})


def about(request):
	return render(request, 'home/about.html', {
		'page_title': 'Про Нас'
	})


def contacts(request):
	if request.method == "GET":
		return render(request, 'home/contacts.html', {
			'page_title': 'Контакти'
		})
	elif request.method == "POST":
		feedback_form = FeedbackForm(request.POST)
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		if feedback_form.is_valid():
			subject = "Відгук з сайту LaunchIT"
			body = f"""
				<h1>Повідомлення про відгук з сайту LauchIT</h1>
				<hr>
				<h2 style="color: black">Ім'я користувача: {name}</h2>
				<h2 style="color: black">E-Mail користувача: {email}</h2>
				<h2 style="color: black">Текст відгуку: \n{message}</h2>
			"""
			try:
				send_mail(subject, '', 'LaunchIT', [email], fail_silently=False, html_message=body)
			except BadHeaderError:
				return HttpResponse('Некоректний заголовок!')
			return render(request, 'home/thank_feed.html', {
				'page_title': 'Відгук',
				'email': email
			})


def news(request):
	page_size = 2
	all_news = News.objects.all()

	paginator = Paginator(all_news, page_size)
	page_number = request.GET.get('page')
	paginate_news = paginator.get_page(page_number)

	return render(request, 'home/news.html', {
		'page_title': 'Новини',
		'all_news': all_news,
		'paginate_news': paginate_news
	})


class NewsDetailView(View):
	def get(self, request, slug):
		n = News.objects.get(url=slug)
		return render(request, 'home/post.html', {
			'n': n,
			'page_title': 'Тема ->'
		})


