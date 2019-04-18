from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice

# Create your views here.


def index(request):
    qs = Question.objects.all()
    return render(request, 'votetest/index.html', {'qs': qs})


def vote(request, qid):
    q = Question.objects.get(pk=qid)
    # cs = q.choice_set.all()
    return render(request, 'votetest/vote.html', {'q': q})


def addvote(request, qid):
    cid = request.POST['option']
    c = Choice.objects.get(pk=cid)
    c.cpoll += 1
    c.save()
    q = Question.objects.get(pk=qid)
    q.qpoll += 1
    q.save()
    return HttpResponseRedirect('/votetest/detail/'+str(qid)+'/', {'qid': qid})


def detail(request, qid):
    q = Question.objects.get(pk=qid)

    return render(request, 'votetest/detail.html', {'q': q})

