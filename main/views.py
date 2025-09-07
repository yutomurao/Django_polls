from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("おはよう！藤原先生！")

def hobby(request):
    return HttpResponse("私の趣味は野球観戦です。")

def greet(request, name):
    message = "こんにちは ", name, " さん！！"
    return HttpResponse(message)