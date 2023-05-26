from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('app1 string1')
def htstring(request):
    return render(request,'second.html')
