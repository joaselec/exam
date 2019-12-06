#from stock.models import CronLog
import os

a = 0
 
def my_scheduled_job():    
    #CronLog.objects.create()
    #CronLog.save()
    #print("cron")
    fileRW()



def fileRW():
    try:
        global a
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(BASE_DIR, 'cron.txt')
        filename = os.path.basename(filepath)

        # with open(filepath, 'rb') as f:
        #     response = HttpResponse(f, content_type="application/vnd.ms-excel")
        #     response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        f = open(filename, 'a')
        f.write(str(a))
        a = a + 1
    finally:
        f.close()


def my_cron_job():
    #pass
    print("cron")

fileRW()
#my_scheduled_job()