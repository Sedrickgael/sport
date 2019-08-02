"""sport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from sport.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('compte', views.compte, name='compte'),
    path('profile', views.profile, name='profile'),
    path('paris', views.paris, name='paris'),
    path('football', views.football, name='football'),
    path('basketball', views.basketball, name='basketball'),
    path('tenis', views.tenis, name='tenis'),
    path('rugby', views.rugby, name='rugby'),
    path('autres', views.autres, name='autres'),
    path('signup_succes', views.succes, name='succes'),
    path('inscription/', views.inscription, name='inscription'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
