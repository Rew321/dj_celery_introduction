from django.http import HttpResponse
from django.shortcuts import render

from mainapp.tasks import test_func

# Create your views here.
def test(request):
    """Call test_func asynchronously and return a response with "Done"."""
    test_func.delay()
    return HttpResponse("Done")
