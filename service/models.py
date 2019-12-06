from django.db import models

# Create your models here.
from userauth.models import User


class Sample(models.Model):
    def __str__(self):
        return
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

