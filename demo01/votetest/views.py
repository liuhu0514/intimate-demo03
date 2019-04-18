from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.


def index(request):
    return HttpResponse('首页')


def vote(request):
    return HttpResponse('投票')

def detail(request):
    return HttpResponse('详情')

