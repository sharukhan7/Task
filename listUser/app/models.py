from turtle import title
from django.db import models

# Create your models here.
class user(models.Model):
    company = models.CharField(max_length=100,blank=True)
    user_name =  models.CharField(max_length=100,blank=True)
    user_email = models.EmailField(null=True)

    class meta():
        db_table = 'user'

class corporate(models.Model):
    company_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(null=True)
    job_title = models.CharField(max_length=100,null=True)

    corporate_user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)

    class meta():
        db_table ='Corporate'