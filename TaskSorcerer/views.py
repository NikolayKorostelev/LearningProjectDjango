from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

menu = ['Главная', 'Список дел', 'Добавить задачу', 'обратная связь']

# Create your views here.
def main(request):
    data = {
        'title':'Главная страница',
        'menu': menu,
    }

    return render(request, '../templates/TaskSorcerer/main.html', context=data)

def login(request):
    return render(request, '../templates/TaskSorcerer/login.html')

