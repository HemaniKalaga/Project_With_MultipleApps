from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rcb(request):
    return render(request,'templatesrcb.html')

def rcb(request):
    return HttptResponse('<h1>This is HttpResponse page of rcb</h1>')
