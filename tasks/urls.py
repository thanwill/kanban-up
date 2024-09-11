from django.urls import path, include
from . import views as tasks

app_name = 'tasks'
urlpatterns = [
    path("", tasks.index, name="index"),
    path("add/", tasks.add_task, name="add_task"),
]