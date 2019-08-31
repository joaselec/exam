from django.db import models


# Create your models here.
class result(models.Model):
    objects = models.Manager()
    session_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    title_id = models.CharField(max_length=10)
    example_id = models.CharField(max_length=10)
    select_id = models.CharField(max_length=10)
    check_yn = models.CharField(max_length=1)    

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.session_id, self.user_name, self.date, self.title_id, self.example_id, self.check_yn, self.select_id)


class Header(models.Model):
    update_at = models.DateTimeField('UpdateAt')
 
class Detail(models.Model):
    header = models.ForeignKey(Header, on_delete=models.PROTECT)
    purchase_date = models.DateField('Date')
    name = models.CharField('Name', max_length=255)
    price = models.DecimalField('Price', max_digits=10, decimal_places=0)