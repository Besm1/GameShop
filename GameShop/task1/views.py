from itertools import repeat

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister

# Create your views here.

users = {'vasya':('dadadada',20), 'petya':('dadadada',19), 'masha':('netnetnet',19)}
info = {}
form = None

def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'username: {username}')
        print(f'password: {password}')
        print(f'age: {age}')

        error = True

        info['username'] = username
        info['password'] = password
        info['repeat_password'] = repeat_password
        info['age'] = age

        info['error'] = ''

        if username in [u_.lower() for u_ in users.keys()]:
            info['error'] += 'Имя пользователя занято. Попробуйте другое. * '
        if repeat_password != password:
            info['error'] += 'Пароли не совпадают. Попробуйте ещё раз.'
        if not info['error']:
            users[username] = (password, age)
            return HttpResponse(content=f'Вы успешно зарегистрировались! Приветствуем, {username}!')

        return render(request,'registration_page.html',context = info)

    return render(request, 'registration_page.html')

def sign_up_by_django(request):
    global form

    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            info = {'form': form, 'error': ''}

            if username in [u_.lower() for u_ in users.keys()]:
                info['error'] += 'Имя пользователя занято. Попробуйте другое. * '
            if repeat_password != password:
                info['error'] += 'Пароли не совпадают. Попробуйте ещё раз.'
            if not info['error']:
                users[username] = (password, age)
                return HttpResponse(content=f'Вы успешно зарегистрировались! Приветствуем, {username}!')
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'registration_page_dj.html', context=info)

class AutoShop(TemplateView):
    template_name = 'AutoShop_main.html'

class Service(TemplateView):
    template_name = 'service_price.html'
    extra_context = {'services':['Поездка за город с пьянкой и плясками под луной negligee      ... 15 000 руб./час ...'
        , "Заправка под завязку фирменным коктейлем и виски из самовара ...  5 000 руб./чел. ..."
        , 'ВНИМАНИЕ -- АКЦИЯ!!! Поездка в любом направлении без пьянки и песнопений ... Бесплатно!!! ...'
                                 ]}

class SpareParts(TemplateView):
    template_name = 'parts_price.html'
    extra_context = {'parts':["Руль спортивный из рогов антилопы гну ... извините, нет в продаже ..."
                     , "Шланг бензиновый                      ... извините, не завезли    ..."
                     , 'Коктейль фирменный "Эх, прокачу!" ... 500 руб. ...'
                     , 'Виски "Johnny Driver" ... 750 руб. ...'
                     ]}
