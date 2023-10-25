from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .song import Song
from .playlist_handler import PlaylistHandler

#instantiates a playlist handler outside the functions so there is no need to create a new one every time
playlist_handler = PlaylistHandler()

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def analysis(request):
    playlist_link = request.POST.get('playlist_link')

    playlist = playlist_handler.get_playlist(playlist_link)

    context = {
        'playlist': playlist,
        'avg_values': playlist.get_avg_attributes(),
    }

    template = loader.get_template('analysis.html')
    return HttpResponse(template.render(context, request))