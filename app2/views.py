from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string2(request):
    return HttpResponse('string2')
def htstring2(request):
    return render(request,'second.html')
