# Ex02 Django ORM Web Application
## Date: 14/10/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Create an app in the Django Project Folder

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Football_player,Football_playerAdmin
admin.site.register(Football_player,Football_playerAdmin)

model.py
from django.db import models
from django.contrib import admin
class Football_player (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    height=models.IntegerField()
    weight=models.IntegerField()

class Football_playerAdmin(admin.ModelAdmin):
    list_display=['name','age','email','height','weight']
```    
## OUTPUT
![Alt text](<Screenshot (1).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
