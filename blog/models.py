from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    contactNo = models.CharField(max_length=12)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100,default="user")

    def __int__(self):
        return self.firstName

class Leave(models.Model):
    leaveId = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, editable=True)

    def __int__(self):
        return self.leaveId


