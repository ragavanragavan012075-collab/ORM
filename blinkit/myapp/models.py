from django.db import models
from django.contrib import admin 
class blinkit(models.Model):
    Name=models.CharField(max_length=10)
    Address=models.TextField()
    Productname=models.CharField(max_length=10)
    quantity=models.IntegerField()
    rate=models.IntegerField()
    phone_number=models.IntegerField(primary_key=True)
    Emailid=models.EmailField()
class blinkitadmin(admin.ModelAdmin):
    list_display=["Name","Address","Productname","quantity","rate","phone_number","Emailid"]