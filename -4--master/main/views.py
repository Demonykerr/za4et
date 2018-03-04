from django.shortcuts import render
from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha


# Create your views here.

from requests import request


def index(request):
    return render(request, 'zach/home.html')

def start(request):
    return render(request, 'zach/start.html')


def journals(request):
    return render(request, 'zach/left_menu/journals.html')

def library(request):
    return render(request, 'zach/left_menu/library.html')

def feedback(request):
    return render(request, 'zach/right_menu/feedback.html')

def information(request):
    return render(request, 'zach/right_menu/information.html')
