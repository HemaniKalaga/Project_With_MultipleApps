
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def csk(request):
    return render(request,'templatescsk.html')

def csk(request):
    return HttpResponse('This is HttpResponse page of csk') 