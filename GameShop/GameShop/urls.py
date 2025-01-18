"""
URL configuration for Game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import Shop, Goods, Basket, sign_up_by_django, shop_entry, news

urlpatterns = [
    path('admin/', admin.site.urls)
    , path('', shop_entry)
    , path('shop/', Shop.as_view())
    , path('shop/goods/', Goods.as_view())
    , path('shop/basket/', Basket.as_view())
    , path('register/',sign_up_by_django)
    , path('platform/news/',news)
]
