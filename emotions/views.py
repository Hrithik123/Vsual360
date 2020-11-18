from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'emotions/vsual.html')
    
def index2(request):
    return render(request,'emotions/vsual2.html')

def index3(request):
    return render(request,'emotions/vsual3.html')