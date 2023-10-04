from django.urls import path

from tasks import views

urlpatterns =[
    path('add-task/', views.create_task, name='add-task'),
    path('list-taks/', views.user_task, name ='list-of-taks'),
    path('delete-task/<int:pk>', views.DeleteViewTask.as_view(), name='delete-task'),
    path('update-task/<int:task_id>',views.update_task, name = 'update_task'),
    path('detail-task/<int:pk>', views.DetailTask.as_view(), name ='detail_task'),
    path('mark-done/<int:task_id>', views.mark_as_done, name ='mark-done')

]