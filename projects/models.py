from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.utils import timezone

from members.models import MemberUser
from notifications.models import Notifications


# Create your models here.

class Project(models.Model):
    project_status = [
        ('Planned', 'planned'),
        ('In Progress', 'in progress'),
        ('On Hold', 'on hold'),
        ('Completed', 'completed')
    ]
    priority_project = [
        ('Low', 'low'),
        ('High', 'high'),
        ('Medium', 'medium')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=None)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=30, choices=project_status)
    priority = models.CharField(max_length=30, choices=priority_project)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    team_members = models.ManyToManyField(MemberUser, related_name='team_project')

    def __str__(self):
        return self.name

    def check_deadline(self):
        """inregistrez notificarea cand proiectul ajunge la deadline"""
        if self.end_date <= timezone.now():
            notification = Notifications(receiver=self.owner,
                                         message=f"Your project '{self.name}' reached the deadline!")
            notification.save()
