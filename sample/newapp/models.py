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