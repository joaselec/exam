from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class board(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    detail = RichTextField()
    hits = models.IntegerField(default=0)
    write_date = models.CharField(max_length=255)
    modify_date = models.CharField(max_length=255)
    enable_yn = models.CharField(max_length=1)
    #recommend = models.CharField(max_length=500)

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.username, self.title, 
        self.detail, self.hits, self.write_date, self.modify_date, self.enable_yn)