# VIEWS

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))
    # return HttpResponse('Oh, hi! Current server time is... s%' % now)


def sorted_numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted susccesfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json',)


def say_hi(request, name, age):
    """Return a greeting"""
    name=name.title()
    if age<12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzi'.format(name)

    return HttpResponse(message)