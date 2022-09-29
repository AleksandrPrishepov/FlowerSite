from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name = 'main'),
    path('about', about, name = 'about'),
    path('add_stat', add_stat, name = 'add_stat'),
    path('connect', connect, name = 'connect'),
    path('register', register, name = 'register'),
    path('login/', login_u, name = 'login'),
    path('logout', logout_user, name = 'logout'),
    path('read_flower/<slug:flo_slug>', read_flower, name = 'read_flower'),
    path('category/<slug:categ_slug>', category, name = 'category')
]