from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StaffAddForm

from order.models import *
from authentication.models import *
from skiservice import *
from equipment.models import *

@login_required
def start(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = StaffAddForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = StaffAddForm()
        
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'admin/admin.html', context)

@login_required
def staff(request, slug=None ):
    #article =Order.objects.get(slug=slug)
    return render(request, 'admin/admin_staff.html', {'article': slug})

@login_required
def order(request, slug=None):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = StaffAddForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = StaffAddForm()
    content = {
         'form': form,
        'orders': orders,
        'article': slug,
    }
    return render(request, 'admin/admin.html',content)
