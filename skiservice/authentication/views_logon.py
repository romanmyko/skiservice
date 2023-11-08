from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import CustomUser



def index(request):
    messages = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
       
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active :
                print('ddd')
                login(request, user)
                if user.role == 0:
                    role_select = 'user_panel'
                elif user.role == 1:
                    role_select = 'admin_panel'
                return redirect(f'{role_select}')
            else:
                messages = 'User or password incorect'
    else:
        form = LoginForm()
      
    content = {
        'form': form,
        'messages': messages,
    }
    
    return render(request, 'index.html', content)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            role = int(form.cleaned_data['user_type'])

            if CustomUser.objects.filter(email=email).exists():
                return render(request, 'register.html', {'form': form, 'user_exists': True})

            user = CustomUser.objects.create_user(
                email=email,
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                middle_name=form.cleaned_data['middle_name'],
                role=role,
                is_active = True,
            )

            login(request, user)
            if role == 1:
                role_select = 'admin_panel'
            else:
                role_select = 'user_panel'
                
            return redirect(f'{role_select}')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
