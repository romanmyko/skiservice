from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import CustomUser


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            get_authenticate = CustomUser.objects.filter(email=email).first()
            if get_authenticate is not None and check_password(password, get_authenticate.password):
                if get_authenticate.role == 1:
                    return redirect('admin_panel')
                else:
                    role_select = 'user_panel'
                return redirect(f'/{role_select}/{get_authenticate.id}')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return render(request, 'register.html', {'form': form, 'user_exists': True})

            user = CustomUser.objects.create_user(
                email=email,
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                middle_name=form.cleaned_data['middle_name'],
                role=form.cleaned_data['user_type']
            )
            role = int(form.cleaned_data['user_type'])
            if role == 1:
                role_select = 'admin_panel'
                return redirect(f'/{role_select}')
            else:
                role_select = 'user_panel'
          #  login(request, user)
            return redirect(f'/{role_select}/{user.id}')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
