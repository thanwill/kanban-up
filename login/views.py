from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from forms.forms import LoginForm


@csrf_exempt
def index(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Autenticar o usuário (o Django autentica normalmente pelo username, então vamos buscar o usuário pelo email)
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)  # Loga o usuário
                    return redirect('/tasks')  # Redireciona para outra página após login
                else:
                    print("Senha incorreta")
            except User.DoesNotExist:
                print("Usuário não encontrado")

    return render(request, 'login/index.html', {'form': form})

