from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Trick

def index(request):
    latest_trick_list = Trick.objects.order_by('-pub_date')[:5]
    template = loader.get_template('catalog/index.html')
    context = RequestContext(request, {
        'latest_trick_list': latest_trick_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)