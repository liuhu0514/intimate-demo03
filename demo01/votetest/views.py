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


def delete(request, qid):
    Question.objects.get(pk=qid).delete()
    return HttpResponseRedirect('/votetest/')


def edit(request, qid):
    q = Question.objects.get(pk=qid)
    return render(request, 'votetest/edit.html', {'q': q})


def editres(request, qid):
    q = Question.objects.get(pk=qid)
    q.qname = request.POST['qname']
    q.save()
    cs = q.choice_set.all()
    for c in cs:
        c.cname = request.POST[str(c.id)]
        c.save()
    return HttpResponseRedirect('/votetest/')


def add(request):
    return render(request, 'votetest/add.html')


def addres(request):
    qname = request.POST['qname']
    c1name = request.POST['c1']
    c2name = request.POST['c2']
    q = Question()
    q.qname = qname
    q.save()
    c1 = Choice()
    c1.cname = c1name
    c1.cque = q
    c1.save()
    c2 = Choice()
    c2.cque = q
    c2.cname = c2name
    c2.save()
    return HttpResponseRedirect('/votetest/')


def addchoice(request, qid):
    q = Question.objects.get(pk=qid)
    return render(request, 'votetest/addchoice.html', {'q': q})


def addchoicehandle(request, qid):
    q = Question.objects.get(pk=qid)
    Choice.objects.create(cname=request.POST['cname'], cque=q).save()
    return HttpResponseRedirect('/votetest/edit/'+str(qid)+'/', {'q': q})


def deletechoice(request, cid):
    c = Choice.objects.get(pk=cid)
    q = c.cque
    c.delete()
    return HttpResponseRedirect('/votetest/edit/' + str(q.id) + '/', {'q': q})
