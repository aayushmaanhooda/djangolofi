from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    song_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=50)
    tags = models.CharField(max_length=20)
    image = models.ImageField(upload_to='docs')
    song = models.FileField(upload_to='docs')
    credit = models.CharField(max_length=1000 , default='')

    def __str__(self):
        return self.name
    

class watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User , on_delete = models.CASCADE)
    vedio_id = models.CharField(max_length=1000 , default='')
    

class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User , on_delete = models.CASCADE)
    music_id = models.CharField(max_length=1000 , default='')
    