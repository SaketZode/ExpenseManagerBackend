from django.db import models
from Friendlist.models import Friend
from Users.models import Account


class Lending(models.Model):
    User = models.ForeignKey(Account, on_delete=models.CASCADE)
    Particulars = models.CharField(max_length=150)
    Amount = models.PositiveIntegerField()
    Description = models.TextField(max_length=500)
    Friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    Status = models.BooleanField()
