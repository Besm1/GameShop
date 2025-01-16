"""
URL configuration for GameShop project.

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
from ..task1.views import
from task1.views import func_template, ClassTemplate
# from task3.views import AutoShop, Service, SpareParts
from task4.views import AutoShop, Service, SpareParts
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),

    , path('', func_template)
    , path('class/', ClassTemplate.as_view())
    , path('autoshop/', AutoShop.as_view())
    , path('autoshop/service/', Service.as_view())
    , path('autoshop/parts/', SpareParts.as_view())
    , path('sendhtml/',sign_up_by_html)
    , path('senddj/',sign_up_by_django)
]
