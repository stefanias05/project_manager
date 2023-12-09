# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MemberUser(User):
    position = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='member_profile/', null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
