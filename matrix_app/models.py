from django.db import models

# Create your models here.
class usr_register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=10)
    myfile = models.FileField(upload_to='usr/')
class dr_register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField(auto_now=False)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    myfile = models.FileField(upload_to='dr/')
    qualfication = models.CharField(max_length = 50,default = 'IOM')
    field = models.CharField(max_length = 20 ,default = "Neurologist")