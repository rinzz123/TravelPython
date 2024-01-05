from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People


# Create your views here.



def demo1(request):
    obj=Place.objects.all()
    person=People.objects.all()
    return render(request,"index.html",
                  {'result':obj,'people':person})

