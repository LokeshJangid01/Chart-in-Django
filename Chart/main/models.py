from django.db import models

# Create your models here.
class Editor(models.Model):
    name = models.CharField(max_length=200)
    num_users = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.num_users) 
