"""
URL configuration for MyDjangoProject project.

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
from task1.views import home, shop_games, cart, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform', home, name='home'),  # Главная страница
    path('shop/', shop_games, name='shop'),  # Магазин
    path('cart/', cart, name='cart'),  # Корзина
    path('sign_dj/', sign_up_by_django, name='sign_up_by_django'),  # Django
]
