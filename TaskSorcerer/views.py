from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import json

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

def reg(request):
    with open('TaskSorcerer/static/city.json', 'r', encoding='utf-8') as file:
        cities_data = json.load(file)
        cities = cities_data["cities"]
    return render(request, '../templates/TaskSorcerer/reg.html', {'cities': cities})

def main1(request):
    return render(request, '../templates/TaskSorcerer/main1.html')

def lessons(request):
    return render(request, '../templates/TaskSorcerer/lessons.html')




