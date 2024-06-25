"""ingredients"""
from django.http import HttpResponse


def welcome(request):
    """example"""
    # print(dir(request))
    return HttpResponse("Welcome to my Calorizer")
