from django.urls import path

from notifications import views

urlpatterns =[
    path('notifications/',views.view_notifications, name='notifications')
]