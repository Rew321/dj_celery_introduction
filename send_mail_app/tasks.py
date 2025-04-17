from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task
from django.core.mail import send_mail

from CORE import settings
from django.utils import timezone
from datetime import timedelta

@shared_task
def test_func():
    #operation
    for i in range(10):
        print(i)
    return "Done"


@shared_task(bind=True)
def send_mail_func(self):
    #operation
    users = get_user_model().objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = 'Hello from Celery'
        message = 'Hello there, this app was created using Django and Celery with Redis to send emails.'
        to_email = user.email
        send_mail(mail_subject,
                  message, 
                  from_email= settings.EMAIL_HOST_USER,
                  recipient_list=[to_email],
                  fail_silently=False
                  )
    return "Done with email send"