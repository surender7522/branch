from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import loader, Context
from branch_change.models import Choice,Poll

def index(request):
    poll_list = Poll.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'poll_list': poll_list,
    })
    return HttpResponse(t.render(c))

def post_list(request):
    return redirect( 'branch_change.views.lin' )


def details(request, poll_id):
    poll_list = Poll.objects.all()
    t = loader.get_template('details.html')
    c = Context({
        'poll_list': poll_list,
    })
    return HttpResponse(t.render(c))


def results(request, poll_id):
    return render_to_response('results.html')


def vote(request, poll_id):
    return render_to_response('vote.html')
def create_user( request ):
    if request.POST:
        u = request.POST['username']
        p = request.POST['password']
        e = request.POST['email']
        user = User.objects.create_user( u, e, p)
        return redirect( 'branch_change.views.lin' )
    return render(request, 'branch_change/create.html' )

def lin(request):
    if request.POST:
        print( request.POST )
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate( username=u, password=p )
        if user is not None:
            if user.is_active:
                login( request, user )
                return redirect('branch_change.views.post_list')
    return render(request, 'branch_change/login.html', {})

def lout( request ):
    logout( request )
    return redirect( 'branch_change.views.lin' )