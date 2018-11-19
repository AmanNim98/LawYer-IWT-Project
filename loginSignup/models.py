from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.name + ":" + self.email

class contactUs(models.Model):
    name = models.CharField(max_length = 100, null = True, blank = True)
    phone = models.BigIntegerField( null = True, blank = True)
    email = models.EmailField( null = True, blank = True)
    country = models.CharField(max_length =  50, null = True, blank = True)
    subject = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name + ":" + self.email

