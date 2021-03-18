from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    html = "<h1>Hello, world!</h1>"
    return HttpResponse(html)