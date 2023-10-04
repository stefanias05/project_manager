from datetime import timezone

from django.db import models

from members.models import MemberUser
from projects.models import Project


# Create your models here.
class Task(models.Model):
    priority_task = [
        ('Low', 'LOW'),
        ('Medium', 'MEDIUM'),
        ('High', 'HIGH')
    ]
    status_task =[
        ('To do', 'TO DO'),
        ('In progress', 'IN PROGRESS'),
        # ('Completed', 'COMPLETED')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    status = models.CharField(max_length=100,choices=status_task)
    priority = models.CharField(max_length=100, choices=priority_task)
    deadline = models.DateField()
    user = models.ForeignKey(MemberUser, on_delete=models.CASCADE, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
