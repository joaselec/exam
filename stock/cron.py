from stock.models import CronLog
 
def my_scheduled_job():    
    CronLog.objects.create()
    #CronLog.save()
    print("cron")

a = 0

def fileRW():
    try:
        global a
        f = open("test.txt", 'a')
        f.write(str(a))
        a = a + 1
    finally:
        f.close()


def my_cron_job():
    #pass
    print("cron")