from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from forms.forms import LoginForm, RegisterForm


@csrf_exempt
def index(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)  # Loga o usuário
                    return redirect('/tarefas')  # Redireciona para outra página após login
                else:
                    print("Senha incorreta")
            except User.DoesNotExist:
                print("Usuário não encontrado")
    return render(request, 'login/login.html', {'form': form})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']

            if password == password_confirmation:
                try:
                    user = User.objects.create_user(username=email, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('/')
                except Exception as e:
                    print(e)
            else:
                print("As senhas não conferem")

    return render(request, 'login/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
