from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def registration(request):
    if request.method == 'GET':
        return render(request, 'account/registration.html', {
            'page_title': 'Реєстрація'
        })
    elif request.method == 'POST':
        # 1. Зчитуємо з форми реєстраційні дані:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        exist_username = User.objects.filter(username=username).exists()
        exist_email = User.objects.filter(email=email).exists()
        if exist_username:
            message = 'Логін зайнятий!'
        elif exist_email:
            message = 'E-Mail зайнятий!'
        elif password2 != password1:
            message = 'Паролі не співпадають!'
        else:
            new_user = User.objects.create_user(username, email, password1)
            message = f'{new_user} ви успішно зареєстровані!'
    return render(request, 'account/reg_res.html', {
        'page_title': 'Звіт про реєстрацію',
        'message': message
    })


def confirm(request):
    return render(request, 'account/confirm.html', {
        'page_title': 'Підтвердження'
    })


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html', {
            'page_title': 'Вхід'
        })
    elif request.method == 'POST':
        _username = request.POST.get('username')
        _password1 = request.POST.get('password1')
        check_user = authenticate(request, username=_username, password=_password1)
        if check_user is None:
            message = 'Користувач не знайдений!'
        else:
            message = f'{_username} Ви успішно авторизовані!'
            login(request, check_user)
        return render(request, 'account/entry_res.html', {
            'page_title': 'Звіт про авторизацію',
            'message': message
        })


def ajax_check_username(request):
    response = dict()
    username = request.GET['username']
    response['message_username'] = username
    users_check = User.objects.filter(username=username)
    if len(users_check) >= 1:
        response['ajax_message'] = "Ok"
        response['quntity'] = len(users_check)
    else:
        response['ajax_message'] = "not Ok"
        response['quntity'] = len(users_check)
    return JsonResponse(response)


def ajax_check_email(request):
    response = dict()
    email = request.GET['email']
    response['message_email'] = email
    email_check = User.objects.filter(email=email)
    if len(email_check) >= 1:
        response['ajax_message'] = "Ok"
        response['quntity'] = len(email_check)
    else:
        response['ajax_message'] = "not Ok"
        response['quntity'] = len(email_check)
    return JsonResponse(response)


def out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'account/profile.html', {
        'page_title': 'Профіль'
    })


def reset(request):
    return render(request, 'account/reset.html', {
        'page_title': 'Реєстрація'
    })
