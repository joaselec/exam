from django.db import models

# Create your models here.
class itemCode(models.Model):
    objects = models.Manager()
    item = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    

    def __str__(self):
        return "%s %s" % (self.item, self.code)

class CronLog(models.Model):
    objects = models.Manager()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        #return self.date.ctime()
        return self.date.__str__
        
        