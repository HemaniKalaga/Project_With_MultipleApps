from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'templatesmsd.html')

def msd(request):
    return HttpResponse('This is HttpResponse page of msd')