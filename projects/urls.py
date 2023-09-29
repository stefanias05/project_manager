from django.urls import path

from projects import views

urlpatterns=[
    path('create_project/', views.CreateProjectView.as_view(), name='create-project'),
    path('list_of_projects/', views.ListProjectView.as_view(), name='list-of-projects'),
    path('delete_project/<int:pk>/', views.DeleteProjectView.as_view(), name='delete-project'),
    path('update_project/<int:pk>/', views.UpdateProjectView.as_view(), name ='update-project'),
    path('detail_project/<int:project_id>/', views.detail_project, name='detail-project'),
    path('add_members_project/<int:project_id>', views.allocate_member_project, name = 'add-members-project'),
    path('my_projects/', views.user_project, name ='my-projects'),


]