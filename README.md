# Ex02 Django ORM Web Application
## Date: 10/10/2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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
admin.py
from django.contrib import admin
from.models import blinkit,blinkitadmin
admin.site.register(blinkit,blinkitadmin)
 ```


## OUTPUT
<img width="1920" height="1080" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/3237541f-c159-483f-9bf4-13351000c00b" />



## RESULT
Thus the program for creating vehicle service Database using ORM hss been executed successfully.
