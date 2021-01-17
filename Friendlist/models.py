from django.db import models
from Users.models import Account


class Friend(models.Model):
    User = models.ForeignKey(Account, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Name
