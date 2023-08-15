from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .song import Song

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def analysis(request):
    playlist_link = request.POST.get('playlist_link')

    #create a test song object
    song = Song("https://open.spotify.com/track/7wBJfHzpfI3032CSD7CE2m?si=2c92617d97284914")
    
    #print the song artist
    print(song.artist)

    context = {
        'playlist_link': song.artist,

    }

    template = loader.get_template('analysis.html')
    return HttpResponse(template.render(context, request))