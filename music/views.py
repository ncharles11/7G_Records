from django.shortcuts import render
from .models import Artiste, Chanson

def home(request):
    artistes = Artiste.objects.all()# 2 artistes en vedette
    return render(request, 'music/home.html', {'artistes': artistes})

def artists(request):
    artistes = Artiste.objects.all()
    return render(request, 'music/artists.html', {'artistes': artistes})

def music(request):
    artistes = Artiste.objects.prefetch_related('chansons').all()
    return render(request, 'music/music.html', {'artistes': artistes})

def about(request):
    return render(request, 'music/about.html')