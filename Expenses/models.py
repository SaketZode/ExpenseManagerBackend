from django.db import models
from Users.models import Account
# Create your models here.


class Expenses(models.Model):
    User = models.ForeignKey(Account, on_delete=models.CASCADE)
    Particulars = models.CharField(max_length=200)
    Amount = models.PositiveIntegerField()
    Date = models.DateField()

