from django.urls import path

from members import views

urlpatterns = [
    path('create_user/', views.MemberAccountForm.as_view(), name='create-member'),
    path('team/', views.MembersListView.as_view(), name='team-members'),
    path('member/<int:member_id>/completed_projects/', views.completed_member_project, name='completed-projects'),
    path('edit_profile/', views.UpdateUserView.as_view(), name='edit-profile')

]
