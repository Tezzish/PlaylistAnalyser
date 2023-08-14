from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import spotipy

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def analysis(request):
    playlist_link = request.POST.get('playlist_link')

    context = {}

    template = loader.get_template('analysis.html')
    return HttpResponse(template.render(context, request))