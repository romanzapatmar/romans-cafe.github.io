from django.db import models

#makemigrations -create changes and stored in a file
#migrate -apply the pending changes in the created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    comments = models.TextField()
    date = models.DateField()

    #it will return the name of the object
    def __str__(self):
        return self.name
