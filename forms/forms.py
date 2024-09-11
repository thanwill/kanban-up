from django import forms
from django.contrib.auth.models import User

class TaskForm(forms.Form):
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
            ('pendente', 'Pendente'),
            ('andamento', 'Em andamento'),
            ('concluida', 'Concluída'),
            ('cancelada', 'Cancelada'),
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

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Usuários' # Altera o label do campo task_users
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
