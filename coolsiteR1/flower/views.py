from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from flower.models import *
from flower.forms import *
menu = ({'name':"О сайте",'url_name':'about'},
        {'name':"Добавить статью", 'url_name':'add_stat'},
        {'name':"Обратная связь", 'url_name':'connect'})


def main(request):
    context = {'title':'Главная страница',
               'menu': menu,
               'cat_selected':0,
               'page_number': request.GET.get('page')
               }
    return render(request, 'flower/index.html', context=context)

def category(request, categ_slug):
    flo = Flower.objects.filter(cat__slug=categ_slug).select_related('cat')
    context = {'title': 'Категории',
               'menu': menu,
               'flo': flo,
               'cat_selected': flo[0].cat_id,
               'categ_slug':categ_slug,
               'page_number': request.GET.get('page')
               }
    return render(request, 'flower/index.html', context=context)

def read_flower(request, flo_slug):
    flo = Flower.objects.get(slug=flo_slug)
    context = {'title': 'О растениях',
               'menu': menu,
               'flo': flo,
               'cat_selected': flo.cat_id,
               }
    return render(request, 'flower/read_flower.html', context=context)

def about(request):
    hard_skils = ('Python', 'Django', 'ORM Django', 'СУБД: SQLite')
    context = {'title': 'О сайте',
               'menu': menu,
               'hard_skils':hard_skils}
    return render(request, 'flower/about.html', context=context)

def add_stat(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = FlowerForm()
    context = {'title': 'Добавить статью',
               'menu': menu,
               'form': form,
               }
    return render(request, 'flower/add_state.html', context=context)

def connect(request):
    form = ConnectForm()
    context = {'title': 'Обратная связь',
               'menu': menu,
               'form': form,
               }
    return render(request, 'flower/contact.html', context=context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
        username = request.POST['username']
        password = request.POST['password1']
        new_user = authenticate(request, username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect('main')
    else:
        form = RegisterForm()
    context = {'title': 'Регистрация',
               'menu': menu,
               'form': form
               }
    return render(request, 'flower/register.html', context=context)

def login_u(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    else:
        form = LoginForm()
    context = {'title': 'Войти',
               'menu': menu,
               'form': form,
               }
    return render(request, 'flower/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('777')