from stock.models import CronLog
 
def my_scheduled_job():    
    CronLog.objects.create()
    #CronLog.save()
    print("cron")

def my_cron_job():
    #pass
    print("cron")