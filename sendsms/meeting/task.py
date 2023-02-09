from sendsms.celery import app
from .models import Meeting
from django.conf import settings
#from sendsms import settings
from django.http import HttpResponse
import time
from twilio.rest import Client
from datetime import timedelta,datetime

@app.task(name = "send_notification")
def send_notification():

    try:

        meeting_objs = Meeting.objects.filter(date_time = datetime.now().replace(microsecond=0) + timedelta(minutes=10))
        print(meeting_objs)
        #print(datetime.now().replace(microsecond=0) + timedelta(minutes=10))
        #print(datetime.utcfromtimestamp())
        subject = 'Notification for meeting!'
        message = "Your have a meeting!"
        print(settings.TWILIO_ACCOUNT_SID)
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        print(client)
        for meeting_obj in meeting_objs:
            print(meeting_obj.phone_number)
            #recipient_list = [meeting_obj.phone_number]
            client.messages.create(to=meeting_obj.phone_number,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message)
        return 1
    except Exception as e:
        print(e)
