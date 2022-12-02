from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# The ExpenseCateogy model is a value that
# we can apply to recipets like gas or entertainment.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User,
        related_name="categories",
        on_delete=models.CASCADE,
    )


# The Account model is the way that we paid for it,
# such as with a specific credit card
# or bank account
class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(
        User,
        related_name="accounts",
        on_delete=models.CASCADE,
    )


# The Receipt model is the primary thing that
# this app keeps trask of for account purposes
class Receipt(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    tax = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey(
        User,
        related_name="receipts",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        ExpenseCategory, related_name="receipts", on_delete=models.CASCADE
    )
    account = models.ForeignKey(
        Account,
        related_name="receipts",
        on_delete=models.CASCADE,
        null=True,
    )
