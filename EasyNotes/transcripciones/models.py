from django.db import models
from django.contrib.auth.models import User

class Transcripciones(models.Model):
    title = models.CharField(max_length=100)
    transcripcion = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
 

class Resumen(models.Model):
    resumen = models.TextField()
    transcripcion = models.ForeignKey(Transcripciones, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class FechasImportantes(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

def __str__(self):
    return self.text