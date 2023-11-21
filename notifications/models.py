from django.contrib.auth.models import User
from django.db import models

from members.models import MemberUser


# Create your models here.

class Notifications(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    message_read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

