from django.db import models

# Create your models here.
class SignupModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=30)
    contact_no = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    cnf_password = models.CharField(max_length=10)
