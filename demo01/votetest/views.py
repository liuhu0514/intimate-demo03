from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.


def index(request):
    temp = loader.get_template('votetest/index.html')
    temp = temp.render()
    return HttpResponse(temp)


def vote(request):
    temp = loader.get_template('votetest/vote.html')
    temp = temp.render()
    return HttpResponse(temp)

def detail(request):

    return render(request, 'votetest/detail.html')

