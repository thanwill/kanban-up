from django import forms
from django.contrib.auth.models import User

from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'task_title',
            'placeholder': 'Digite o título da tarefa',
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'task_description',
            'rows': 3,
            'placeholder': 'Digite a descrição da tarefa',
        })
    )
    status = forms.ChoiceField(
        choices=(
            ('TODO', 'Em andamento'),
            ('DONE', 'Concluída'),
            ('CANCELLED', 'Cancelada'),
            ('BLOCKED', 'Bloqueada'),
            ('BACKLOG', 'Backlog'),
        ),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'task_status',
        })
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'task_users',
        })
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'id': 'task_due_date',
            'type': 'date',
        })
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'user', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Usuários'  # Altera o label do campo task_users
        self.fields['user'].required = False
        self.fields['due_date'].required = False

    def save(self):
        pass


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'user_email',
            'aria-describedby': 'emailHelp',

        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'user_password',
        })
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'first_name',
            'placeholder': 'Digite seu nome',
        })
    )
    last_name = forms.CharField(
        max_length=30,
        label='Sobrenome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'last_name',
            'placeholder': 'Digite seu sobrenome',
        })
    )
    email = forms.EmailField(
        max_length=254,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'user_email',
            'aria-describedby': 'emailHelp',
            'placeholder': 'Digite seu email',
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'user_password',
            'placeholder': 'Digite sua senha',
        })
    )
    password_confirmation = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'user_password_confirmatio',
            'placeholder': 'Confirme sua senha',
        })
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('As senhas não conferem')
        return cleaned_data

    def save(self):
        pass


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'comment',
            'rows': 3,
            'placeholder': 'Digite seu comentário',
        })
    )

    def save(self):
        pass
