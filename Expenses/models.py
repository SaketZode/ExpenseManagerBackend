from django.db import models
from Users.models import Account


class Expenses(models.Model):
    User = models.ForeignKey(Account, on_delete=models.CASCADE)
    Particulars = models.CharField(max_length=200)
    Amount = models.PositiveIntegerField()
    Date = models.DateField()
    Status = models.BooleanField()

