from django.shortcuts import render
from django.http import HttpResponse

"""
Views:
    Function-based views:
     eg   def hello(request):
            return HttpResponse("Hello World!")
        

    Class-based views:
     eg   class AboutView(TemplateView):
            template_name = "about.html"

"""

def hello(request):
    return HttpResponse("Hello World!")