from itertools import repeat

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


from .forms import UserRegister
from .models import Buyer, Game, News
from utils.password_utils import hash_password

# Create your views here.


# users = {'kolya':('dadadada',20), 'petya':('dadadada',19), 'masha':('netnetnet',19)}
info = {}
form = None

def shop_entry(request):
    return render(request, 'shop_entry.html')

def news(request):
    posts = News.objects.all().order_by('-date')
    paginator = Paginator(object_list=posts, per_page=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})


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

            if Buyer.objects.all().filter(name=username):
                info['error'] += 'Имя пользователя занято. Попробуйте другое. * '
            if repeat_password != password:
                info['error'] += 'Пароли не совпадают. Попробуйте ещё раз.'
            if not info['error']:
                # users[username] = (password, age)

                Buyer.objects.create(name=username, password=hash_password(password=password), age=age, balance = 0)
                return HttpResponse(content=f'Вы успешно зарегистрировались! Приветствуем, {username}!')

    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'registration_page_dj.html', context=info)

class Shop(TemplateView):
    template_name = 'Shop_main.html'

class Basket(TemplateView):
    template_name = 'basket.html'
    extra_context = {'services':['Поездка за город с пьянкой и плясками под луной negligee      ... 15 000 руб./час ...'
        , "Заправка под завязку фирменным коктейлем и виски из самовара ...  5 000 руб./чел. ..."
        , 'ВНИМАНИЕ -- АКЦИЯ!!! Поездка в любом направлении без пьянки и песнопений ... Бесплатно!!! ...'
                                 ]}

class Goods(TemplateView):
    template_name = 'price_list.html'
    goods = Game.objects.all()
    extra_context = {'goods': goods}
    # extra_context = {'parts':["Руль спортивный из рогов антилопы гну ... извините, нет в продаже ..."
    #                  , "Шланг бензиновый                      ... извините, не завезли    ..."
    #                  , 'Коктейль фирменный "Эх, прокачу!" ... 500 руб. ...'
    #                  , 'Виски "Johnny Driver" ... 750 руб. ...'
    #                  ]}


