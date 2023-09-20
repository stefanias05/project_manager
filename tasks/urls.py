from django.urls import path

from tasks import views

urlpatterns =[
    path('add-task/', views.CreateTask.as_view(), name='add-task'),
    path('list-taks/', views.user_task, name ='list-of-taks'),
    path('delete-task/<int:pk>', views.DeleteViewTask.as_view(), name='delete-task')

]