from django.shortcuts import render
from django.http import HttpResponse

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('меня зовут Даулет учусь в гиикс')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('Домашние животные – это животные, которых люди содержат дома для общения, удовольствия или помощи. Они могут быть разными по виду, характеру и целям содержания')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse('19;51')
