from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def form_validation(request):
    SO=StudentForm()
    d={'SO':SO}
    if request.method=='POST':
        SO1=StudentForm(request.POST)
        if SO1.is_valid():
            return HttpResponse(str(SO1.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    return render(request,'form_validation.html',d)
