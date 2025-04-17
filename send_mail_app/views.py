import json
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_mail_func, test_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
# Create your views here.
def test(request):
    """Call test_func asynchronously and return a response with "Done"."""
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_users(request):
    send_mail_func.delay()
    return HttpResponse("mail sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=11, minute=35
    )
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name = "schedule_mail_task" + "5", task="send_mail_app.tasks.send_mail_func")#, args=json.dumps(([[2,3]])))
    return HttpResponse("mail scheduled")