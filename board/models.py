from django.db import models

# Create your models here.
class board(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=5000)
    hits = models.IntegerField(max_length=10)
    #recommend = models.CharField(max_length=500)

    def __str__(self):
        return "%s %s %s %s" % (self.username, self.title, 
        self.detail, self.hits)