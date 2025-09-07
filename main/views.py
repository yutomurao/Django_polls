from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("おはよう！藤原先生！")