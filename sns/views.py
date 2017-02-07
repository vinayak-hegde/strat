from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from .models import Album

def login(request):
    return render(request,'login.html',{'right_now':datetime.utcnow()})


def hpage(request):
    return render(request,'index.html',{'right_now':datetime.utcnow()})

def mark(request):
    return render(request,'market.html',{'right_now':datetime.utcnow()})


def prof(request):
    all_albums = Album.objects.all()
    context ={
        'all_albums':all_albums,
        }
    return render(request,'profile.html',context)
