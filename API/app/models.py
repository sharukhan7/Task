from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

#To create custom user use email as priority instead of user
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(null=False,max_length=50)
    last_name = models.CharField(null=False,max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

#Income
class Categories(models.Model):
    incometype = models.CharField(max_length=30)
    def __str__(self):
        return self.incometype
class Incomemodel(models.Model):
    monthly_income = models.PositiveIntegerField()
    category = models.ForeignKey(Categories, related_name='typeofincome', on_delete=models.CASCADE)
    date = models.DateField()


    class Meta:
      db_table = 'Income_data'
    def __str__(self):
        return self.salary

#Expense
class Expensetype(models.Model):
    expense_type = models.CharField(max_length=50)
    def __str__(self):
        return self.expense_type

class Expensemodel(models.Model):
    expense = models.PositiveIntegerField()
    expensetype = models.ForeignKey(Expensetype, related_name='expenses', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
          db_table = 'Expense_data'
