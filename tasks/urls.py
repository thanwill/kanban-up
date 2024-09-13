from django.urls import path

from . import views as tasks

app_name = 'tasks'
urlpatterns = [
    path("", tasks.task_list, name="index"),
    path("add/", tasks.add_task, name="add_task"),
    path("delete/<int:task_id>/", tasks.delete_task, name="delete_task"),
    path('edit/<int:task_id>/', tasks.edit_task, name='edit_task'),
    path("list/", tasks.task_list, name="task_list"),
    path("atualizar/<int:task_id>/<int:user_id>/", tasks.change_user, name="change_user"),
    path("comentario/<int:task_id>/", tasks.add_comment, name="add_comment"),

]