from django.shortcuts import render, redirect
from .form import SubscribeForm


def subscribe(request):
	form = SubscribeForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/')
