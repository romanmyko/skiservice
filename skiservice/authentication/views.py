from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from order import *
from authentication import *
from skiservice import *

@login_required
def start(request):
    return render(request, 'skiservice.html')
