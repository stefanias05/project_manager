from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

from members.models import MemberUser


# from members.models import MemberUser


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
    description = models.TextField( null=True)
    start_date = models.DateField(null=None)
    end_date = models.DateField(null=None)
    status = models.CharField(max_length=30, choices=project_status)
    priority = models.CharField(max_length=30, choices=priority_project)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    team_members = models.ManyToManyField(MemberUser, related_name='team_project')


    def __str__(self):
        return self.name
