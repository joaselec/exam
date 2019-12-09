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

class stocks(models.Model):
    objects = models.Manager()
    stock_code = models.CharField(max_length=255)
    stock_name = models.CharField(max_length=255)
    start_price = models.CharField(max_length=255)
    current_price = models.CharField(max_length=255,null=True)
    stock_returns =  models.CharField(max_length=255,null=True)
    update_date = models.DateTimeField(max_length=255,null=True)

    def __str__(self):
        return "%s %s %s %s %s" % (self.stock_code, self.stock_name, self.start_price, self.current_price, self.stock_returns)
        
        