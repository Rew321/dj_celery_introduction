from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_mail_func, test_func
# Create your views here.
def test(request):
    """Call test_func asynchronously and return a response with "Done"."""
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_users(request):
    send_mail_func.delay()
    return HttpResponse("mail sent")